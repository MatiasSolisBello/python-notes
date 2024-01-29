# -*- coding: utf-8 -*-
"""03. Dictionaries.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13sAUyfVAlQ1SGRsQaGLEZrs_pUxnNZ0U
"""

"""
Ejercicio 1

Escribir un programa que guarde en una variable el diccionario
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y
muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""
currencies = {
    'Euro':'€',
    'Dollar':'$',
    'Yen':'¥'
}

word = input('enter a currency: ')
if word.title() in currencies:
    print(currencies.get(word.title()))
else:
    print('Currency is not avaible')

"""
Ejercicio 2

Escribir un programa que pregunte al usuario su nombre, edad, dirección y
teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el
mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono
es <teléfono>.
"""
name = input('enter your name: ')
age = input('enter your age: ')
address = input('enter your address: ')
phone_number = input('enter your phone number: ')

data = {
    'name': name, 'age': age, 'address': address, 'phone_number': phone_number
}

print(f"{data['name']}, has {data['age']} years old, live in {data['address']} "
    f"and his phone number is {data['phone_number']}")

"""
Ejercicio 3

Escribir un programa que guarde en un diccionario los precios de frutas,
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el
precio de ese número de kilos de fruta. Si la fruta no está en el diccionario
debe mostrar un mensaje informando de ello.
"""
fruits = {
    'Banana': 1.35,
    'Apple': 0.80,
    'Pear': 0.85,
    'Orange': 0.70
}

fruit_choose = input('Enter a fruit: ').title()
kg_choose = float(input('Enter a kg. : '))

if fruit_choose in fruits:
    price = float(fruits[fruit_choose]) * kg_choose
    print('The price is: $', price)
else:
    print('Fruit is not available')

"""
Ejercicio 4

Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por
pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre
del mes.
"""
date = input('Introduce a date in dd/mm/yyyy format ')
date = date.split('/')
print(date[0], 'de', date[1], 'de', date[2])

"""
Ejercicio 5

Escribir un programa que almacene el diccionario con los créditos de las
asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después
muestre por pantalla los créditos de cada asignatura en el formato <asignatura>
tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas
del curso, y <créditos> son sus créditos. Al final debe mostrar también el
número total de créditos del curso.
"""
subjects = {
    'Math': 6,
    'Physics': 4,
    'Chemistry': 5
}

total_credits = 0
for key, value in subjects.items():
    total_credits += value
    print(f'{key} has {value} credits')
print(f'The course has {total_credits} credits')

"""
Ejercicio 6

Escribir un programa que cree un diccionario vacío y lo vaya llenado con
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono,
correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un
nuevo dato debe imprimirse el contenido del diccionario.
"""
person = {}
next_question = True

while next_question:
    key = input('¿What piece of information do you want to add? ')
    value = input(key + ': ')
    person[key] = value
    print(person)
    next_question = input('¿Do you want add more information (y/n)? ') == "y"

"""
Ejercicio 7

Escribir un programa que cree un diccionario simulando una cesta de la compra.
El programa debe preguntar el artículo y su precio y añadir el par al
diccionario, hasta que el usuario decida terminar. Después se debe mostrar por
pantalla la lista de la compra y el coste total, con el formato Articulo-Precio
"""
data = {}
next_question = True
total = 0
while next_question:
    item = input('What object do you want to buy?')
    price = int(input('What is the price if this object? $ '))
    total += price
    data[item] = price
    next_question = input('Do you want add another object (y/n)? ') == "y"

print('--- Shopping list ---')
for key, value in data.items():
    print(f'* {key} :    ${value}')
print('TOTAL: $', total)

"""
Ejercicio 8

Escribir un programa que cree un diccionario de traducción español-inglés. El
usuario introducirá las palabras en español e inglés separadas por dos puntos, y
cada par <palabra>:<traducción> separados por comas. El programa debe crear un
diccionario con las palabras y sus traducciones. Después pedirá una frase en
español y utilizará el diccionario para traducirla palabra a palabra. Si una
palabra no está en el diccionario debe dejarla sin traducir.
"""
dic = {}
word = input('Enter a word <spanish>:<english>: ')
#print(word.split(','))
for i in word.split(','):
    key, value = i.split(':')
    dic[key] = value
phrase = input('Enter a phrase in Spanish: ')
for i in phrase.split():
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(i, end=' ')

"""
Ejercicio 10

Escribir un programa que permita gestionar la base de datos de clientes de una
empresa. Los clientes se guardarán en un diccionario en el que la clave de cada
cliente será su NIF, y el valor será otro diccionario con los datos del cliente
(nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el
valor True si se trata de un cliente preferente. El programa debe preguntar al
usuario por una opción del siguiente menú: (1) Añadir cliente,
(2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes,
(5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida
el programa tendrá que hacer lo siguiente:

    1. Preguntar los datos del cliente, crear un diccionario con los datos y
        añadirlo a la base de datos.
    2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
    3. Preguntar por el NIF del cliente y mostrar sus datos.
    4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
    5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y
        nombre.
    6. Terminar el programa.

"""