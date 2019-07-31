#!python
from collections import deque
import heapq

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""

class Vertex(object):

    def __init__(self, vertex):
        """Initialize a vertex and its neighbors.
        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def __eq__(self, vertex):
        return self.id == vertex

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return self.id

    def add_neighbor(self, vertex, weight=0):
        """Add a neighbor along a weighted edge."""
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight
            return True

        return False

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        
        return [neighbor for neighbor,_ in self.neighbors.items()]

    def get_id(self):
        """Return the id of this vertex."""
        return self.id

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        try:
            return self.neighbors[vertex]
        except KeyError:
            return "Vertex {} not in Graph".format(vertex.id)


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""

class Graph:
    def __init__(self):
        """Initialize a graph object with an empty dictionary, number of edges and vertices"""
        self.graph = {}
        self.edges = 0
        self.vertices = 0

    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax: for v in g"""
        return iter(self.graph.values())

    def add_vertex(self, key):
        """Add a new vertex object to the graph with the given key and return the vertex.
            Time & Space complexity : O(1) | O(1)
        """
        vertex = Vertex(key)
        self.vertices += 1
        self.graph[key] = vertex

        return vertex

    def get_vertex(self, key):
        """Return the vertex if it exists
            Time & Space Complexity : O(1) | O(1)
        """

        vertex = None
        try: 
           vertex = self.graph[key]
        except KeyError:
            raise ValueError("Vertex with key {} not in Graph".format(key))

        return vertex


    def add_edge(self, key1, key2, weight=0):
        """add an edge from vertex with key `key1` to vertex with key `key2` with a cost."""

    
        if key1 not in self.graph and key2 not in self.graph:
            raise ValueError("Both Vertex of keys {} and {} not in Graph".format(key1, key2))
        elif key1 not in self.graph or key2 not in self.graph:
            raise ValueError("Either Vertex of keys {} and {} not in Graph".format(key1, key2))

        elif key1 == key2:
            raise ValueError("Vertex {} can't be its own neighbor".format(key1))
        else:
            # Get the two neighbor verteces
            vertex_one = self.graph[key1]
            vertex_two = self.graph[key2]

            # Code idea from Vicenzo : https://github.com/C3NZ/CS22/blob/master/challenges/graph.py#L77
            added_from = vertex_one.add_neighbor(vertex_two, weight)
            added_to = vertex_two.add_neighbor(vertex_one, weight)

            if added_from and added_to:
                self.edges += 1

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.graph.keys()


def depth_first_search(graph, origin, destination, visited=None):
    """DFS to determine if there is a path between two vertices in a weighted directed graph
    """

    if not visited:
        visited = set()

    if origin == destination:
        return True

    visited.add(origin)
    neighbors = origin.get_neighbors()
   
    for neighbor in neighbors:
        if neighbor not in visited:
            if depth_first_search(graph, neighbor, destination, visited):
                return True
                
    return False


def breadth_first_search(graph, vertex_key):
    """
        Return all nodes that are exactly n connections away from vertex.
    """
    if vertex_key not in graph:
        return

    visited_vertices = set()
    vertex = graph.get_vertex(vertex_key)
    graph_queue = deque([vertex])
    visited_vertices.add(vertex)

    while len(graph_queue) > 0:

        curr_vertex = graph_queue.popleft()
        adj_vertices = curr_vertex.get_neighbors()
        remaining_elements = set(adj_vertices).difference(visited_vertices)
        if len(remaining_elements) > 0:

            for elem in remaining_elements:
                visited_vertices.add(elem)
                graph_queue.append(elem)

    return visited_vertices

def find_path(graph, from_vert, to_vert, visited=None):
    
    if not visited:
        visited = []

    if (from_vert not in graph) or (to_vert not in graph):
        return None

    visited.append(from_vert)
    if from_vert == to_vert:
        return True


    neighbors = graph.get_vertex(from_vert).get_neighbors()

    for neighbor in neighbors:
        if neighbor not in visited:
            if find_path(graph, neighbor, to_vert, visited):
                return visited
    return None

def shortest_path(graph, origin, destination):

    graph_queue = deque([origin])
    distances = { vertex: -1 for vertex in graph}
    distances[origin] = 0

    while len(graph_queue) > 0:
        curr_vertex = graph_queue.popleft()
        neighbors = curr_vertex.get_neighbors()
        
        for neighbor in neighbors:
            # if the neighbor has not been visted yet
            if distances[neighbor] == -1:
                # Distance to the neighbor 1 away than the curr_vertex
                distances[neighbor] = distances[curr_vertex] + 1
                graph_queue.append(neighbor) 

    return distances[destination]



# Driver code
if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")

    # Add connections (non weighted edges for now)
    g.add_edge("A", "C")
    g.add_edge("A", "B")
    g.add_edge("B", "A")
    g.add_edge("B", "D")
    g.add_edge("C", "A")
    g.add_edge("C", "E")
    g.add_edge("D", "B")
    g.add_edge("D", "E")
    g.add_edge("E", "C")
    g.add_edge("E", "D")

    origin = g.get_vertex("A")
    destination = g.get_vertex("D")

    print(shortest_path(g, origin, destination))

