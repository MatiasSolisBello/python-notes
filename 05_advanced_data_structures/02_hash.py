"""
Tabla Hash

Estructuras de datos que permiten almacenar y recuperar datos de manera
eficiente. Utilizan una función hash para asignar claves a ubicaciones
específicas en una tabla. Esto facilita el acceso rápido a los datos, ya que la
función hash permite calcular la posición de almacenamiento de un elemento a
partir de su clave.

En Python, las tablas hash se implementan a través de diccionarios (dict).
"""
# Crear una tabla hash (diccionario)
hash_table = {}

# Insertar elementos
hash_table['clave1'] = 'valor1'
hash_table['clave2'] = 'valor2'
hash_table['clave3'] = 'valor3'

# Acceder a elementos
print("Valor para clave2:", hash_table['clave2'])

# Modificar un elemento
hash_table['clave1'] = 'nuevo_valor'

# Eliminar un elemento
del hash_table['clave3']

# Verificar si una clave está en la tabla
print("¿clave3 está en la tabla?", 'clave3' in hash_table)

# Obtener todas las claves
print("Claves en la tabla:", list(hash_table.keys()))
print('------------------')

class HashTable:
    def __init__(self):
        self.size = 10  # Tamaño de la tabla
        self.table = [None] * self.size

    def hash_function(self, key):
        # Ejemplo de función hash simple para claves de tipo cadena
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        # Resolver colisiones mediante encadenamiento (lista en cada celda)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for pair in self.table[index]:
                if pair[0] == key:
                    # Actualizar el valor si la clave ya existe
                    pair[1] = value
                    break
            else:
                # Agregar una nueva entrada si la clave no existe
                self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)

        # Buscar en la lista asociada a la celda
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]

        raise KeyError(key + " no encontrado en la tabla")

# Uso de la tabla hash personalizada
custom_hash_table = HashTable()
custom_hash_table.insert('clave1', 'valor1')
custom_hash_table.insert('clave2', 'valor2')
custom_hash_table.insert('clave3', 'valor3')

print("Valor para clave2:", custom_hash_table.get('clave2'))
