#!python

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

    def add_neighbor(self, vertex, weight=0):
        """Add a neighbor along a weighted edge."""

        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight

        return 

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return "hi"
        #return f'{self.id} adjacent to {[x.id for x in self.neighbors]}'

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return [neighbor for neighbor in self.neighbors.items()]

    def get_id(self):
        """Return the id of this vertex."""
        return self.id

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        # TODO return the weight of the edge from this
        # vertex to the given vertex.
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
        """Initialize a graph object with an empty dictionary."""
        self.vertList = {}
        self.numVertices = 0

    def add_vertex(self, key):
        """Add a new vertex object to the graph with the given key and return the vertex."""
        vertex = Vertex(key)
        self.numVertices += 1
        self.vertList[key] = vertex

        return vertex

    def get_vertex(self, key):
        """Return the vertex if it exists"""
        try:
            return self.vertList[key]
        except KeyError:
            print("Vertex Not found in Network")

    def add_edge(self, key1, key2, cost=0):
        """add an edge from vertex with key `key1` to vertex with key `key2` with a cost."""
        # TODO if either vertex is not in the graph,
        # add it - or return an error (choice is up to you).
        # TODO if both vertices in the graph, add the
        # edge by making t a neighbor of f
        # and using the addNeighbor method of the Vertex class.
        # Hint: the vertex f is stored in self.vertList[f].

        try:
            if not self.vertList[key1] and not self.vertList[key2]:
                return "Both Vertexes not in Graph"
            elif not self.vertList[key1] or not self.vertList[key2]:
                return "One of the Vertext not in Graph."
            else:
                vertext_one = Vertex(key1)
                vertext_two = Vertex(key2)
                vertext_one.add_neighbor(vertext_two)
                return

        except KeyError:
            return "Vertex not in Graph"

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()

    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax: for v in g"""
        return iter(self.vertList.values())


# Driver code


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.add_vertex("Jeorge")
    g.add_vertex("Lofi")
    g.add_vertex("Obama")
    g.add_vertex("Josh")
    g.add_vertex("Medi")
    g.add_vertex("Crawford")
    g.add_vertex("Reagan")
    g.add_vertex("Elf")
    g.add_vertex("Rob")


    # Add connections (non weighted edges for now)
    g.add_edge("Jeorge", "Obama")
    g.add_edge("Jeorge", "Lofi")
    g.add_edge("Jeorge", "Reagan")
    g.add_edge("Rob", "Obama")
    g.add_edge("Rob", "Crawford")
    g.add_edge("Obama", "Josh")
    g.add_edge("Josh", "Medi")
    g.add_edge("Obama", "Medi")
    g.add_edge("Crawford", "Lofi")
    g.add_edge("Crawford", "Elf")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.get_vertices())

    # Print edges
    # print("The edges are: ")
    # for v in g:
    #     for w in v.get_neighbors():
    #         print("( %s , %s )" % (v.getId(), w.getId()))
