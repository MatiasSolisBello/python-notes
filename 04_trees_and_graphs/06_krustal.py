"""
Algoritmo de Kruskal

Se utiliza para encontrar el árbol de expansión mínima de un grafo conectado,
ponderado y no dirigido
"""
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                self.rank[root2] += 1


def kruskal(graph):
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            edges.append((vertex, neighbor, weight))

    # Ordenar las aristas por peso
    edges.sort(key=lambda x: x[2])

    # Conjunto disjunto para mantener los conjuntos de vértices conectados
    disjoint_set = DisjointSet(graph.keys())

    # Árbol de expansión mínima
    minimum_spanning_tree = []

    for edge in edges:
        vertex1, vertex2, weight = edge
        if disjoint_set.find(vertex1) != disjoint_set.find(vertex2):
            disjoint_set.union(vertex1, vertex2)
            minimum_spanning_tree.append(edge)

    return minimum_spanning_tree


# Ejemplo de uso
# Grafo ponderado representado como un diccionario de diccionarios
graph = {
    'A': {'B': 2, 'D': 3},
    'B': {'A': 2, 'D': 4, 'E': 3},
    'C': {'F': 2},
    'D': {'A': 3, 'B': 4, 'E': 5},
    'E': {'B': 3, 'D': 5, 'F': 1},
    'F': {'C': 2, 'E': 1}
}

# Obtener el árbol de expansión mínima
minimum_spanning_tree = kruskal(graph)

# Imprimir los resultados
print("Aristas en el árbol de expansión mínima:")
for edge in minimum_spanning_tree:
    print(f"{edge[0]} - {edge[1]}: {edge[2]}")
