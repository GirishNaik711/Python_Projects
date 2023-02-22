import random

class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjecent = {}
        self.neighbors = []
        self.neighbor_weights = []


    def add_edge_to(self, vertex, weight=0):
        self.adjecent[vertex] = weight

    def increment_edge(self, vertex):
        self.adjecent[vertex] = self.adjecent.get(vertex, 0) +1

    def get_adjacent_nodes(self):
        pass

    # initializes probability map   
    def get_probability_map(self):
        for(vertex, weights) in self.adjecent.items():
            self.neighbors.append(vertex)
            self.neighbor_weights.append(weights)

    def next_word(self):
        return random.choices(self.neighbors, weights=self.neighbor_weights)[0]



class Graph:
    def __init__(self):
        self.vertices = {}

    def get_vertex_values(self):
        return set(self.vertices.keys())

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        if value not in self.vertices:
            self.add_vertex(value)
        return value       

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices:
            vertex.get_probability_map()
