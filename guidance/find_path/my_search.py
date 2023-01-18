
import numpy as np
import heapq
import math

def euclidean(a, b):
    x1, y1 = a
    x2, y2 = b
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

class Graph:
    """A graph connects nodes (vertices) by edges (links). Each edge can also
    have a length associated with it. The constructor call is something like:
        g = Graph({'A': {'B': 1, 'C': 2})
    this makes a graph with 3 nodes, A, B, and C, with an edge of length 1 from
    A to B,  and an edge of length 2 from A to C. You can also do:
        g = Graph({'A': {'B': 1, 'C': 2}, directed=False)
    This makes an undirected graph, so inverse links are also added. The graph
    stays undirected; if you add more links with g.connect('B', 'C', 3), then
    inverse link is also added. You can use g.nodes() to get a list of nodes,
    g.get('A') to get a dict of links out of A, and g.get('A', 'B') to get the
    length of the link from A to B. 'Lengths' can actually be any object at
    all, and nodes can be any hashable object."""

    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.locations_dict = {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    def make_undirected(self):
        """Make a digraph into an undirected graph by adding symmetric edges."""
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.connect1(b, a, dist)

    def connect(self, A, B, distance=1):
        """Add a link from A and B of given distance, and also add the inverse
        link if the graph is undirected."""
        self.connect1(A, B, distance)
        if not self.directed:
            self.connect1(B, A, distance)

    def connect1(self, A, B, distance):
        """Add a link from A to B of given distance, in one direction only."""
        self.graph_dict.setdefault(A, {})[B] = distance

    def get(self, a, b=None):
        """Return a link distance or a dict of {node: distance} entries.
        .get(a,b) returns the distance or None;
        .get(a) returns a dict of {node: distance} entries, possibly {}."""
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    def nodes(self):
        """Return a list of nodes in the graph."""
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)
    
    def neighbors(self, node):
        return self.graph_dict[node].keys()

    def cost(self, a, b):
        return self.graph_dict[a][b]
        
    def heuristic(self, a, b):
        return euclidean(self.locations_dict[a], self.locations_dict[b])

# Create graph from clusters
class End:
    def __init__(self, location, end_id = None, group_id = None):
        self.location = location
        self.group_id = group_id
        self.id = end_id 
class Edge:
    def __init__(self, cluster):
        self.ends = [End(cluster[0]), End(cluster[-1])]
        self.distance = sum([math.dist(cluster[i], cluster[i+1]) for i in range(len(cluster)-1)]) 
        self.cluster = cluster
class Map:
    def __init__(self, clusters, neighbor_cluster_dist, plot_shape):
        
        self.unique_ends = []
        self.fixEnds(clusters, neighbor_cluster_dist)
        self.edges = [Edge(cluster) for cluster in clusters]
        self.graph = self.getGraph()
        self.plot_shape = plot_shape
             
    def fixEnds(self, clusters, neighbor_cluster_dist):
        """if there are ends closer than neighbor_cluster_dist, 
        the ends are replaced by the center of mass of both"""

        # get ends in single list
        ends = []
        for cluster in clusters:
            ends.append(End(cluster[0]))
            ends.append(End(cluster[-1]))

        # get groups of ends closer than neighbor_cluster_dist
        group_ids = []
        for i in range(len(ends)):
            for j in range(i+1, len(ends)):
                if math.dist(ends[i].location, ends[j].location) < neighbor_cluster_dist:
                    if ends[i].group_id is not None:
                        ends[j].group_id = ends[i].group_id
                    else:
                        ends[i].group_id = i
                        ends[j].group_id = i
                        group_ids.append(i)

        # replace ends by center of mass
        for group_id in group_ids:
            group = [end for end in ends if end.group_id == group_id]
            center_of_mass = self.centerOfMass(group)
            for end in group:
                end.location = center_of_mass

        # replace ends in clusters
        for i in range(len(clusters)):
            clusters[i][0] = ends[2*i].location
            clusters[i][-1] = ends[2*i+1].location
    
    def centerOfMass(self, list_of_ends):
        """returns the center of mass of a list of Ends"""
        x = sum([end.location[0] for end in list_of_ends])
        y = sum([end.location[1] for end in list_of_ends])
        return (int(round(x/len(list_of_ends))), int(round(y/len(list_of_ends))))

    def getGraph(self):
        """returns a Graph of the edges in the map"""

        # name all ends with same locations with same id
        end_id = 'A'
        self.unique_ends = []
        for edge in self.edges:
            for end in edge.ends:
                if end.id is None:
                    end.id = end_id
                    self.unique_ends.append(end)
                    for other_edge in self.edges:
                        for other_end in other_edge.ends:
                            if other_end.id is None and other_end.location == end.location:
                                other_end.id = end_id
                    end_id = chr(ord(end_id) + 1)
                    
        graph = Graph(graph_dict=None, directed=False)
        for edge in self.edges:
            graph.connect(edge.ends[0].id, edge.ends[1].id, edge.distance)
        
        for end in self.unique_ends:
            graph.locations_dict[end.id] = end.location

        return graph
        
# Graph Example
romania_map = Graph(dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99),
    Hirsova=dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142)), 
    directed=False)

romania_map.locations = dict(
    Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531))

# Search
def a_star(graph, start, goal):
    frontier = [(0, start)]  # heap of (f_cost, node)
    came_from = {}  # mapping of node to its parent in the path
    g_cost = {start: 0}  # mapping of node to g_cost (cost to reach node from start)
    f_cost = {start: graph.heuristic(start, goal)}  # mapping of node to f_cost (g_cost + heuristic cost to goal)

    while frontier:
        current = heapq.heappop(frontier)[1]  # get node with lowest f_cost

        if current == goal:
            # construct path and return it
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        for neighbor in graph.neighbors(current):
            # calculate cost to reach neighbor from start
            cost = g_cost[current] + graph.cost(current, neighbor)

            if neighbor not in g_cost or cost < g_cost[neighbor]:
                # update g_cost and add neighbor to frontier
                g_cost[neighbor] = cost
                f_cost[neighbor] = cost + graph.heuristic(neighbor, goal)
                heapq.heappush(frontier, (f_cost[neighbor], neighbor))
                came_from[neighbor] = current