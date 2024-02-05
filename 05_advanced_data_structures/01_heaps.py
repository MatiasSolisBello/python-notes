"""
Heaps

estructura de datos basada en un árbol binario completo que satisface la
propiedad del heap: para cada nodo i distinto de la raíz, el valor almacenado en
i es mayor (o menor, dependiendo de si es un max-heap o un min-heap) que o igual
a los valores almacenados en sus hijos.
"""
import heapq

# Crear un heap vacío
min_heap = []

# Insertar elementos en el heap
heapq.heappush(min_heap, 4)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 7)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 5)

print("Elementos en el min-heap:", min_heap)

# Extraer y mostrar el elemento mínimo
min_element = heapq.heappop(min_heap)
print("Elemento mínimo extraído:", min_element)

print("Elementos restantes en el min-heap:", min_heap)
