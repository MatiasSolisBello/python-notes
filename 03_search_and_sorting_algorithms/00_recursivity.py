"""
Recursividad

Hace referencia a problemas en los cuales, dicho problema es parte de la
solución. Se trata de un modelo matemático cuya definición incluye a sí mismo
“se autodefine”; es decir que se llama a sí misma repetidamente hasta que
satisface una determinada
condición para evitar caer en un bucle infinito, y donde cada resultado depende
de la resolución de la siguiente o anterior repetición, hasta alcanzar dicha
condición de fin. Entonces, este modelo recursivo tiene dos características
fundamentales para ser denominado como tal:

1. Debe tener al menos una condición clara de fin o caso base del problema,
puede tener más de una de ser necesario.

2. Debe llamarse a sí mismo, es decir que el modelo o solución sea parte de su
propia definición. Esta llamada puede ser única, si se llama una sola vez dentro
de la función, o múltiple, si se realizan más de una llamada.
"""

# Ejemplo
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
print('factorial: ', factorial(5))


# 1.- Implementar una función que permita obtener el valor en la sucesión de
# Fibonacci para un número dado
def fibonacci(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
print('fibonacci: ', fibonacci(6))


# 2.- Implementar una función que calcule la suma de todos los números enteros
# comprendidos entre cero y un número entero positivo dado.
def sum_numbers(num):
    if num < 0:
        return 0
    else:
        return num + sum_numbers(num-1)
print('sum_numbers: ', sum_numbers(5))


# 3.- Implementar una función para calcular el producto de dos números enteros dados.
#def get_product(num):
#    if num < 0:
#        return 0
#    else:
#        return num + sum_numbers(num-1)
#print('sum_numbers: ', get_product(5, 2))


# 4.- Implementar una función para calcular la potencia dado dos números enteros,
# el primero representa la base y segundo el exponente
def get_power(base, exp):
    return base ** exp
print('get_power I: ', get_power(5,2))

def get_power_with_recursivity(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * get_power_with_recursivity(base, exp - 1)

print('get_power II: ', get_power_with_recursivity(5,2))


# 5.- Desarrollar una función que permita convertir un número romano en un número
# decimal.
def get_roman_number_to_decimal(num_roman):
    data = {
        'I':  1,
        'V': 5,
        'X': 10,
        'L': 50
    }
    return data[1]

print('Roman number: ', get_roman_number_to_decimal('X'))