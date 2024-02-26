5#Realice un programa que calcule X números aleatorios en un rango determinado por el usuario.

import random
#Este módulo proporciona funciones para trabajar con números aleatorios en Python

print('\nPUNTO 2-B')
print('Realice un programa que calcule X números aleatorios en un rango determinado por el usuario.\n')

Rango_Incicial = int(input('Ingrese el valor inicial del rango: '))
Rango_Final = int(input('Ingrese el valor final del rango: '))
Numeros_Aleatorios = int(input('Ingrese cantidad de numeros: '))

#randint(a, b): Devuelve un número entero aleatorio en el rango [a, b], incluyendo a y b.
N_Aleotorio = [random.randint(Rango_Incicial,Rango_Final) for _ in range (Numeros_Aleatorios)]

print('Se genero numeros aleatorios en el rango(',Rango_Incicial,' - ',Rango_Final,')')
print(N_Aleotorio)
