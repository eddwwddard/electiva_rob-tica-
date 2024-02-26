#Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos
#matrices previamente inicializadas.

import numpy as npi #importamos biblioteca NumPy como asignacion np 

# en lugar de escribir numpy.array() podmeos escribir np.array()
#NumPy es una de las bibliotecas más utilizadas en Python para realizar operaciones numéricas y matriciales de manera eficiente. 
print('\nPUNTO 2-A')
print('Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos matrices previamente inicializadas:\n')

#Defino matrices
Matriz_1 = npi.array([[1, 5, 3],[9, 6, 2],[2, 5, 8]])
Matriz_2 = npi.array([[8, 12, 24],[30, 64, 76],[11, 32, 8]])

#matriz_a = np.array([[1,5,3],[9,6,2],[2,5,8]])
#matriz_b = np.array([[8,12,24],[30,65,76],[11,32,8]])

#imprimo matricez
print('Matriz #1:\n',Matriz_1)
print('\n')
print('Matriz #2:\n',Matriz_2)
print('\n')

#Suma
Suma_B = Matriz_1 + Matriz_2
print('Suma de matriz (+):\n', Suma_B)
print('\n')

#Resta
Resta_C = Matriz_1 - Matriz_2
print('Resta de matriz (-):\n', Resta_C)
print('\n')

#Prdoucto punto
ProductoP = npi.dot(Matriz_1,Matriz_2)
print('Producto punto (.):\n',ProductoP) #resultado es un punto en el examen 
print('\n')

#Producto cruz 
ProductoC = npi.cross(Matriz_1,Matriz_2)
print('Producto cruz (X):\n',ProductoC)  #
print('\n')

#Division
Division_A = Matriz_1/Matriz_2
print('Division de matriz (/):\n',Division_A)
print('\n')
