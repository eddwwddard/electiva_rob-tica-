#Realice un programa que calcule X números aleatorios en un rango determinado por el usuario.

import numpy as np

while True:
    try:
        cant = int(input("ingrese la cantidad de numeros aleatorios que desea generar: \n"))
        break
    except ValueError:
        print("ingrese una cantidad valida")
num = np.random.randint(low=-10000000,high=10000000, size=cant, dtype=int)

print('la lista de numeros generada es: \n')
for numeros in num:
    print(numeros)

