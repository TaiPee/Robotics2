import numpy as np
import heapq
import math

# list of possible end ids
END_IDS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ', 'BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BK', 'BL', 'BM', 'BN', 'BO', 'BP', 'BQ', 'BR', 'BS', 'BT', 'BU', 'BV', 'BW', 'BX', 'BY', 'BZ', 'CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG', 'CH', 'CI', 'CJ', 'CK', 'CL', 'CM', 'CN', 'CO', 'CP', 'CQ', 'CR', 'CS', 'CT', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DA', 'DB', 'DC', 'DD', 'DE', 'DF', 'DG', 'DH', 'DI', 'DJ', 'DK', 'DL', 'DM', 'DN', 'DO', 'DP', 'DQ', 'DR', 'DS', 'DT', 'DU', 'DV', 'DW', 'DX', 'DY', 'DZ', 'EA', 'EB', 'EC', 'ED', 'EE', 'EF', 'EG', 'EH', 'EI', 'EJ', 'EK', 'EL', 'EM', 'EN', 'EO', 'EP', 'EQ', 'ER', 'ES', 'ET', 'EU', 'EV', 'EW', 'EX', 'EY', 'EZ', 'FA', 'FB', 'FC', 'FD', 'FE', 'FF', 'FG', 'FH', 'FI', 'FJ', 'FK', 'FL', 'FM', 'FN', 'FO', 'FP', 'FQ', 'FR', 'FS', 'FT', 'FU', 'FV', 'FW', 'FX', 'FY', 'FZ', 'GA', 'GB', 'GC', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GJ', 'GK', 'GL', 'GM', 'GN', 'GO', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GV', 'GW', 'GX', 'GY', 'GZ', 'HA', 'HB', 'HC', 'HD', 'HE', 'HF', 'HG', 'HH','HI', 'HJ', 'HK', 'HL', 'HM', 'HN', 'HO', 'HP', 'HQ', 'HR', 'HS', 'HT', 'HU', 'HV', 'HW', 'HX', 'HY', 'HZ', 'IA', 'IB', 'IC', 'ID', 'IE', 'IF', 'IG', 'IH', 'II', 'IJ', 'IK', 'IL', 'IM', 'IN', 'IO', 'IP', 'IQ', 'IR', 'IS', 'IT', 'IU', 'IV', 'IW', 'IX', 'IY', 'IZ', 'JA', 'JB', 'JC', 'JD', 'JE', 'JF', 'JG', 'JH', 'JI', 'JJ', 'JK', 'JL', 'JM', 'JN', 'JO', 'JP', 'JQ', 'JR', 'JS', 'JT', 'JU', 'JV', 'JW', 'JX', 'JY', 'JZ', 'KA', 'KB', 'KC', 'KD', 'KE', 'KF', 'KG', 'KH', 'KI', 'KJ', 'KK', 'KL', 'KM', 'KN', 'KO', 'KP', 'KQ', 'KR', 'KS', 'KT', 'KU', 'KV', 'KW', 'KX', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LD', 'LE', 'LF', 'LG', 'LH', 'LI', 'LJ', 'LK', 'LL', 'LM', 'LN', 'LO', 'LP', 'LQ', 'LR', 'LS', 'LT', 'LU', 'LV', 'LW', 'LX', 'LY', 'LZ', 'MA', 'MB', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MI', 'MJ', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NB', 'NC', 'ND', 'NE', 'NF', 'NG', 'NH', 'NI', 'NJ', 'NK']

           
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

# Create map from clusters
class End:
    def __init__(self, location, end_id = None, group_id = None):
        self.location = location
        self.group_id = group_id
        self.id = end_id 
class Edge:
    def __init__(self, cluster):
        self.ends = [End(cluster[0]), End(cluster[-1])]
        self.distance = sum([np.linalg.norm(np.array(cluster[i]) - np.array(cluster[i+1])) for i in range(len(cluster)-1)]) 
        self.cluster = cluster
        self.bad = False
class Map:
    def __init__(self, clusters, neighbor_cluster_dist, plot_shape):
        
        # store unique ends
        self.unique_ends = []

        # aglomerate ends closer than neighbor_cluster_dist to same point
        self.fixEnds(clusters, neighbor_cluster_dist)

        # get edges, removing edges that have same ends, but are longer, to bad_edges
        self.edges, self.bad_edges = self.separateEdges(clusters)
        
        # get graph class from edges to use in search
        self.graph = self.getGraph()

        # store plot shape for plotting
        self.plot_shape = plot_shape
    
    def sameEnds(self, edge1, edge2):
        return edge1.ends[0].location == edge2.ends[0].location and edge1.ends[1].location == edge2.ends[1].location

    def sortedEdgeLocs(self, edge):
        return tuple(sorted([edge.ends[0].location, edge.ends[1].location]))

    def separateEdges(self, clusters):
        
        # all edges
        all_edges = [Edge(cluster) for cluster in clusters]

        # name all ends with same locations with same id
        unique_ends = {}
        shorter_edges = {}
        end_id_ix = 0
        # create dict of minimal distance between two equal ends: shorter_edges = {end1,end2: min_distance...}
        for edge in all_edges:
            edge_locs = self.sortedEdgeLocs(edge)
            if edge_locs not in shorter_edges:
                shorter_edges[edge_locs] = edge.distance
            else:
                if shorter_edges[edge_locs] > edge.distance:
                    shorter_edges[edge_locs] = edge.distance
            # create dict of unique ends and give them a unique id: unique_ends = {end.location: end.id... }
            for end in edge.ends:
                if end.location not in unique_ends:
                    end.id = END_IDS[end_id_ix]
                    self.unique_ends.append(end)
                    unique_ends[end.location] = END_IDS[end_id_ix]
                    end_id_ix+=1
                else:
                    end.id = unique_ends[end.location]
        
        # remove edges with same ends, but longer. name ends with same location with same id
        for edge in all_edges:
            edge_locs = self.sortedEdgeLocs(edge)
            if shorter_edges[edge_locs] < edge.distance:
                edge.bad = True
            for end in edge.ends:
                end.id = unique_ends[end.location]

        # separate edges into good and bad
        good_edges = [edge for edge in all_edges if not edge.bad]
        bad_edges = [edge for edge in all_edges if edge.bad]

        return good_edges, bad_edges

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
                if np.linalg.norm(np.array(ends[i].location) - np.array(ends[j].location)) < neighbor_cluster_dist:
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

        graph = Graph(graph_dict=None, directed=False)
        for edge in self.edges:
            graph.connect(edge.ends[0].id, edge.ends[1].id, edge.distance)
        
        for end in self.unique_ends:
            graph.locations_dict[end.id] = end.location

        return graph
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

def getPointsFromPath(path, map):
    edges = map.edges
    points = []
    for i in range(len(path)-1):
        for edge in edges:
            if (edge.ends[0].id == path[i] and edge.ends[1].id == path[i+1]): 
                points.extend(edge.cluster)
                break
            elif (edge.ends[0].id == path[i+1] and edge.ends[1].id == path[i]):
                points.extend(edge.cluster[::-1])
                break
    return points

def getStartEndIDs(map,start_point, end_point):
    """get start and end ids from map.unique_ends that are 
    closest to start_point and end_point"""
    start_id = None
    end_id = None
    start_dist = np.inf
    end_dist = np.inf
    for end in map.unique_ends:
        dist = np.linalg.norm(np.array(end.location) - np.array(start_point))
        if dist < start_dist:
            start_dist = dist
            start_id = end.id
        dist = np.linalg.norm(np.array(end.location) - np.array(end_point))
        if dist < end_dist:
            end_dist = dist
            end_id = end.id
    
    return start_id, end_id

