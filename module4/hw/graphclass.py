"""
Undirected graph class.
"""

class Graph:
    """
    Undirected graph.
    """

    def __init__(self):
        """
        Initializes an empty graph.
        """
        self._graph = {}

    def __str__(self):
        """
        Returns a string representation of the graph.
        """
        return str(self._graph)

    def nodes(self):
        """
        Returns a list of nodes in the graph.
        """
        return list(self._graph.keys())

    def get_neighbors(self, node):
        """
        Returns the neighbor list for node or raises a KeyError if node is not
        in the graph.
        """
        return list(self._graph[node].keys())

    def add_node(self, node):
        """
        Add node to the graph. Does nothing if node is already in the graph.
        """
        if node not in self._graph:
            self._graph[node] = {}

    def add_edge(self, node1, node2, attrs):
        """
        Add an edge between two nodes in the graph, adding the nodes
        themselves if they're not already there.
        """
        ## Update the first node's neighbor list
        if node1 not in self._graph:
            self._graph[node1] = {node2:attrs}
        elif node2 not in self._graph[node1]:
            self._graph[node1][node2] = attrs
        else:
            self._graph[node1][node2] = self._graph[node1][node2].union(attrs)

        ## Update the second node's neighbor list
        if node2 not in self._graph:
            self._graph[node2] = {node1:attrs}
        elif node1 not in self._graph[node2]:
            self._graph[node2][node1] = attrs
        else:
            self._graph[node2][node1] = self._graph[node1][node2].union(attrs)

    def get_attrs(self, node1, node2):
        """
        Given a pair of nodes, returns the attribute of the edge
        between them.  Assumes that there is an edge between the two
        nodes.
        """
        return self._graph[node1][node2]

    def copy(self):
        """
        Returns an identical (deep) copy of the graph.
        """
        g_new = Graph()
        for node in self.nodes():
            for nbr in self.get_neighbors(node):
                for attr in self.get_attrs(node, nbr):
                    g_new.add_edge(node, nbr, attr)
        return g_new


