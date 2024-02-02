"""
Algoritmo de Dijkstra

Se utiliza para encontrar el camino más corto desde un nodo de inicio a todos
los demás nodos en un grafo ponderado dirigido o no dirigido
"""
import heapq

def dijkstra(graph, start):
    # Inicializar distancias con infinito para todos los nodos excepto el nodo de inicio
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Usar una cola de prioridad (heap) para almacenar nodos y sus distancias
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Verificar si esta ruta ya es más larga que la conocida
        if current_distance > distances[current_node]:
            continue

        # Explorar vecinos
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Actualizar la distancia si encontramos un camino más corto
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Ejemplo de uso
# Grafo ponderado representado como un diccionario de diccionarios
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 7},
    'C': {'A': 4, 'F': 5},
    'D': {'B': 2},
    'E': {'B': 7, 'F': 8},
    'F': {'C': 5, 'E': 8}
}

# Nodo de inicio: 'A'
start_node = 'A'

# Obtener distancias más cortas desde el nodo de inicio
shortest_distances = dijkstra(graph, start_node)

# Imprimir los resultados
for node, distance in shortest_distances.items():
    print(f'Distancia más corta de {start_node} a {node}: {distance}')
