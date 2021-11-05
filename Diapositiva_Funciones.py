def suma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print('Ingrese 2 numeros para sumar ')
n1=int(input('Numero 1: '))
n2=int(input('Numero 2: '))

result = suma(n1,n2)

print(f'El resultado de la suma entre {n1} y {n2} es {result}')

cadena = input('Ingrese un valor por teclado: ')

print('Funcion capialize: ', cadena.capitalize())
print('Funcion lower: ', cadena.lower())
print('Funcion upper: ', cadena.upper())

import random, os

print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))
input('Presione una tecla para continuar...')
os.system('cls')