"""
Map Search
"""

import comp140_module7 as maps

class Queue:
    """
    A simple implementation of a FIFO queue.
    """

    def __init__(self):
        """
        Initialize the queue.
        """
        self._queue = []

    def __len__(self):
        """
        Returns: an integer representing the number of items in the queue.
        """
        return len(self._queue)

    def __str__(self):
        """
        Returns: a string representation of the queue.
        """
        return str(self._queue)

    def push(self, item):
        """
        Add item to the queue.

        input:
            - item: any data type that's valid in a list
        """
        self._queue.append(item)

    def pop(self):
        """
        Remove the least recently added item.

        Assumes that there is at least one element in the queue.  It
        is an error if there is not.  You do not need to check for
        this condition.

        Returns: the least recently added item.
        """
        
        return self._queue.pop(0)

    def clear(self):
        """
        Remove all items from the queue.
        """
        self._queue = []

class Stack:
    """
    A simple implementation of a LIFO stack.
    """

    def __init__(self):
        """
        Initialize the queue.
        """
        self._stack = []

    def __len__(self):
        """
        Returns: an integer representing the number of items in the queue.
        """
        return len(self._stack)

    def __str__(self):
        """
        Returns: a string representation of the queue.
        """
        return str(self._stack)

    def push(self, item):
        """
        Add item to the queue.

        input:
            - item: any data type that's valid in a list
        """
        self._stack.append(item)

    def pop(self):
        """
        Remove the least recently added item.

        Assumes that there is at least one element in the queue.  It
        is an error if there is not.  You do not need to check for
        this condition.

        Returns: the least recently added item.
        """
        
        return self._stack.pop()

    def clear(self):
        """
        Remove all items from the queue.
        """
        self._stack = []


def bfs_dfs(graph, rac_class, start_node, end_node):
    """
    Performs a breadth-first search or a depth-first search on graph
    starting at the start_node.  The rac_class should either be a
    Queue class or a Stack class to select BFS or DFS.

    Completes when end_node is found or entire graph has been
    searched.

    inputs:
        - graph: a directed Graph object representing a street map
        - rac_class: a restricted access container (Queue or Stack) class to
          use for the search
        - start_node: a node in graph representing the start
        - end_node: a node in graph representing the end

    Returns: a dictionary associating each visited node with its parent
    node.
    """
    
    algo = rac_class()
    dist = {}
    parent = {}
    
    for node in graph.nodes():
        dist[node] = float("inf")
        parent[node] = None
    dist[start_node] = 0
    algo.push(start_node)
    while len(algo) != 0:
        node = algo.pop()
        for nbr in graph.get_neighbors(node):
            if dist[nbr] == float("inf"):
                dist[nbr] = dist[node] + 1
                parent[nbr] = node
                algo.push(nbr)
                if nbr == end_node:
                    return parent
      
    return parent

def dfs(graph, start_node, end_node, parent):
    """
    Performs a recursive depth-first search on graph starting at the
    start_node.

    Completes when end_node is found or entire graph has been
    searched.

    inputs:
        - graph: a directed Graph object representing a street map
        - start_node: a node in graph representing the start
        - end_node: a node in graph representing the end
        - parent: a dictionary that initially has one entry associating
                  the original start_node with None

    Modifies the input parent dictionary to associate each visited node
    with its parent node
    """
    
    if start_node == end_node:
        return True
    else:
        for node in graph.get_neighbors(start_node):
            if node not in parent:
                parent[node] = start_node
                if dfs(graph, node, end_node, parent):
                    return True
    
    return False

def astar(graph, start_node, end_node,
          edge_distance, straight_line_distance):
    """
    Performs an A* search on graph starting at start_node.

    Completes when end_node is found or entire graph has been
    searched.

    inputs:
        - graph: a directed Graph object representing a street map
        - start_node: a node in graph representing the start
        - end_node: a node in graph representing the end
        - edge_distance: a function which takes two nodes and a graph
                         and returns the actual distance between two
                         neighboring nodes
        - straight_line_distance: a function which takes two nodes and
                         a graph and returns the straight line distance 
                         between two nodes

    Returns: a dictionary associating each visited node with its parent
    node.
    """
    parent = {start_node : None}
    open_set = [start_node]
    closed_set = []
    costs = {start_node : [0, straight_line_distance(start_node, end_node, graph)]}
    
    while len(open_set) != 0:
        # Find the optimal node to search based on least distance to end_node
        optimal_node = open_set[0]
        for node in open_set:
            if (costs[node][0] + costs[node][1]) < (costs[optimal_node][0] + costs[optimal_node][1]):
                optimal_node = node
                
        # Update open_set and parent
        for nbr in graph.get_neighbors(optimal_node):
            g_cost = costs[optimal_node][0] + edge_distance(optimal_node, nbr, graph)
            h_cost = straight_line_distance(nbr, end_node, graph)
            
            # Unexplored nodes
            if (nbr not in closed_set) and (nbr not in open_set):
                parent[nbr] = optimal_node
                open_set.append(nbr)
                costs[nbr] = [g_cost, h_cost]
                
            elif (nbr not in closed_set) and (nbr in open_set):
                if (costs[nbr][0] + costs[nbr][1]) > (g_cost + h_cost):
                    costs[nbr][0] = g_cost
                    parent[nbr] = optimal_node
                    
        closed_set.append(optimal_node)
        open_set.remove(optimal_node)
        
    return parent

maps.start(bfs_dfs, Queue, Stack, dfs, astar)