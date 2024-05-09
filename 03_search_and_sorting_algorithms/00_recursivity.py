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


# 3.- Implementar una función para calcular el producto de dos números enteros
# dados.
def get_product(a, b):
    if a == 0 or b == 0:
        return 0
    if a == 1:
        return b
    if b == 1:
        return a
    if a > 0 and b > 0:
        return a + get_product(a, b - 1)
    if a < 0 and b < 0:
        return -a + get_product(a, b + 1)
    if a < 0:
        return a + get_product(a, b - 1)
    if b < 0:
        return b + get_product(a - 1, b)
print("get_product: ", get_product(5, -3))


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
def get_roman_number_to_decimal(roman_number):
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(roman_number) == 0:
        return 0

    if len(roman_number) == 1:
        return data[roman_number]

    if data[roman_number[0]] < data[roman_number[1]]:
        return data[roman_number[1]] - data[roman_number[0]] + get_roman_number_to_decimal(roman_number[2:])
    else:
        return data[roman_number[0]] + get_roman_number_to_decimal(roman_number[1:])
print("get_roman_number_to_decimal:", get_roman_number_to_decimal('XXIV'))


# 6.- Dada una secuencia de caracteres, obtener dicha secuencia invertida.
def reverse_character_sequence(word):
    if len(word) <= 1:
        return word
    return word[-1] + reverse_character_sequence(word[:-1])
print("reverse_character_sequence:", reverse_character_sequence("Hola Mundo"))


#7.- Desarrollar un algoritmo que permita calcular la siguiente serie:
# h(n) = 1+ 1/2 + 1/3 + ... 1/n


# 8.- Desarrollar un algoritmo que permita convertir un número entero en sistema
# decimal a sistema binario


#9.- Implementar una función para calcular el logaritmo entero de número n en
# una base b

#10.- Desarrollar un algoritmo que cuente la cantidad de dígitos de un número
# entero
def count_digits(num):
    if num < 10 and num >= 0:
        return 1
    return 1 + count_digits(num // 10)
print('count_digits: ', count_digits(100))


#11.- Desarrollar un algoritmo que invierta un número entero sin convertirlo a
# cadena
def reverse_number(num):
    if num < 10 and num >= 0:
        return 1
    return 1 + reverse_number(num // 10)
print('reverse_number: ', reverse_number(100))