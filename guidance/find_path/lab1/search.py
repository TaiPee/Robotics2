import collections
import math
import numpy as np

# print depth of search tree
PRINT_DEPTH = False

# if false, search will also accept solutions that go back in curved lines
GO_BACK_IN_STRAIGHTS = True

# if there are more than this clusters, GO_BACK_IN_STRAIGHS is set to False
GO_BACK_IN_STRAIGHTS_THRESHOLD = 7

# number of times the robot can go back through the cluster
MAX_GO_BACK = 2

class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state. Also includes the total path_cost to reach the node."""

    def __init__(self, state, parent=None, path_cost=0):
        """Create a search tree Node, derived from a parent"""
        self.state = state
        self.parent = parent
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, matrix):
        """List the nodes reachable in one step from this node."""
        
        sequence = self.path()
        current_path = [node.state for node in sequence]
        duplicates = [item for item, count in collections.Counter(current_path).items() if count > MAX_GO_BACK]

        if len(duplicates) > 0:
            return []

        idx = round(self.state)
        children = []
        if self.parent != None:
            before = round(self.parent.state)
            if idx % 2 == 0 and before != idx + 1:
                children.append(Node(idx + 1, self, self.path_cost + 1))
                return children
            elif idx % 2 != 0 and before != idx - 1:
                children.append(Node(idx - 1, self, self.path_cost + 1))
                return children

        neighbours = []
        
        for i in range(len(matrix)):
            if i == idx:
                continue
            elif matrix[idx,i]:
                neighbours.append(i)
        for neighbour in neighbours:
            children.append(Node(neighbour, self, self.path_cost + 1))
        return children

    def solution(self):
        """Return the sequence of actions to go from the root to this node."""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

def intercluster_distance(c1,c2):
    """computes the distance between two clusters, in this case, two end points"""
    return math.dist(np.array(c1), np.array(c2))

def getAdjMatrix(ends, inter_cluster_dist):
    """computes the adjacency matrix between nodes in the tree"""

    matrix = np.zeros((len(ends), len(ends)))

    for i in range(len(ends)):
        if i%2 == 0:
            # nodes from the same cluster are adjacent
            matrix[i,i+1] = 1.0
            matrix[i+1,i] = 1.0
        for j in range(i,len(ends)):
            if i == j:
                # a node is adjacent to itself
                matrix[i,i] = 1.0
            elif intercluster_distance(ends[i],ends[j]) < inter_cluster_dist:
                # adjacent nodes from different clusters
                matrix[i,j] = 1.0
                matrix[j,i] = 1.0
    
    return matrix

def goalTest(sequence, curved_points, nr_nodes):
    """checks if the current path is a goal path"""
    idx = [node.state for node in sequence]

    if PRINT_DEPTH:
        print(len(idx))

    if sequence == None:
        return False
    
    if GO_BACK_IN_STRAIGHTS:
        # list of duplicates
        duplicates = [item for item, count in collections.Counter(idx).items() if count > 1]

        # there can only be duplicates from straight clusters
        if any(i in duplicates for i in curved_points):
            return False
    
    # every node must be in the path
    for i in range(nr_nodes):
        if i not in idx:
            return False
            
    return True

def getOrderedNodes(nodes, matrix, curved_points, important_points):
    """apply bfs in the nodes to find the path to draw"""
    lowest_path = 7+len(nodes)
    final_node = None
    for i in important_points:

        frontier = collections.deque([Node(i)])  # FIFO queue

        while frontier:
            node = frontier.popleft()
            if goalTest(node.path(), curved_points, len(nodes)) and node.path_cost < lowest_path:
                final_node =  node
                frontier.clear()
                break
            frontier.extend(node.expand(matrix))
            if node.depth > lowest_path:
                frontier.clear()
                break
        if final_node != None:
            frontier.clear()
            break

    if final_node == None:
        return None
    else:
        final_path = []
        for node in node.path():
            final_path.append(node.state)
        return final_path
    

    ########################### PATH SEARCH ###########################

def isStraightCluster(cluster):
    """return if cluster is straight or not"""
    
    # if cluster was downsample to 2 points, it's straight
    if len(cluster) == 2:
        return True
    else:
        return False

def separateClusters(clusters):
    """separate straight from curved clusters"""
    straight_clusters = []
    curved_clusters = []

    # if there are too many clusters, assume all are straight search wise
    # this is because the search algorithm is not efficient enough to find 
    # a path only going back in straigh clusters with too many clusters 
    if len(clusters) > GO_BACK_IN_STRAIGHTS_THRESHOLD:
        straight_clusters = [i for i in range(2*len(clusters))]
    else:
        for i in range(0,2*len(clusters),2):
                if isStraightCluster(clusters[round(i/2)]):
                    straight_clusters.append(i)
                    straight_clusters.append(i+1)
                else:
                    curved_clusters.append(i)
                    curved_clusters.append(i+1)
    
    # if there are no straight clusters, assume all are straight search wise
    if len(straight_clusters) == 0:
        straight_clusters = curved_clusters.copy()
        curved_clusters.clear()
    
    return straight_clusters, curved_clusters

def orderRootNodes(ends, starting_points):
    """returns an ordered list that will be used as root nodes"""
    important_points = []

    for i in range(len(ends)):
            if ends[i] in starting_points:
                important_points.append(i)

    for i in range(len(ends)):
        if i not in important_points:
            important_points.append(i)
    
    return important_points
    
def createEnds(clusters):
    """returns the ending points of clusters"""
    ends = []
    for cluster in clusters:
        ends.append(cluster[0])
        ends.append(cluster[-1])
    return ends
        
def createFinalPath(clusters,ends, ends_path):
    """create list of clusters [path] from list of cluster ends [ends], with order given by [ends_path]"""

    path = []
    for i in range(len(ends_path)-1):
        for cluster in clusters:
            if cluster[0] == ends[ends_path[i]] and cluster[-1] == ends[ends_path[i+1]]:
                path.append(cluster)
                break
            elif cluster[-1] == ends[ends_path[i]] and cluster[0] == ends[ends_path[i+1]]:          
                path.append(cluster[::-1])
                break
    
    return path

