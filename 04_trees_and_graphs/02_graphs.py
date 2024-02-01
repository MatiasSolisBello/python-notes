"""
Grafos
"""
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)

    def print_graph(self):
        for vertex, neighbors in self.vertices.items():
            print(f"{vertex}: {', '.join(map(str, neighbors))}")

# Example of usage
example_graph = Graph()

# Add vertices
example_graph.add_vertex(1)
example_graph.add_vertex(2)
example_graph.add_vertex(3)
example_graph.add_vertex(4)

# Add edges
example_graph.add_edge(1, 2)
example_graph.add_edge(2, 3)
example_graph.add_edge(3, 4)
example_graph.add_edge(4, 1)

# Print the graph
example_graph.print_graph()

