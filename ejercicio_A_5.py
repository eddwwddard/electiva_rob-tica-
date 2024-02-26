#Realice en funciones las rotaciones en X, Y y Z, donde se tenga un parámetro de entrada (ángulo)
#y un parámetro de salida (matriz).

import numpy as np   

print('\nPUNTO 5-A')
print('Realice en funciones las rotaciones en X, Y y Z, donde se tenga un parámetro de entrada (ángulo) y un parámetro de salida (matriz).\n')

#Angulos de rotacion 
angulo= np.pi/4  #45 grados 

print('Parametro de entrada: ',angulo,' 45° \n')

def rotacion_x(angulo):
    Cos_X = np.cos(angulo)  # Calculo del coseno del angulo 
    Sin_X = np.sin(angulo)  # Calculo del seno del angulo
    matriz_RX =  np.array([[1,     0,      0],
                           [0, Cos_X, -Sin_X],
                           [0, Sin_X, Cos_X ]])
    return matriz_RX

def rotacion_y(angulo):
    Cos_Y = np.cos(angulo)  # Calculo del coseno del angulo 
    Sin_Y = np.sin(angulo)  # Calculo del seno del angulo
    matriz_RY =  np.array([[ Cos_Y,    0,      Sin_Y],
                           [     0,    1,          0],
                           [-Sin_Y,    0,      Cos_Y]])
    return matriz_RY

def rotacion_z(angulo):
    Cos_Z = np.cos(angulo)  # Calculo del coseno del angulo 
    Sin_Z = np.sin(angulo)  # Calculo del seno del angulo
    matriz_RZ =  np.array([[ Cos_Z,    -Sin_Z,      0],
                           [ Sin_Z,     Cos_Z,      0],
                           [     0,         0,      1]])
    return matriz_RZ

matriz_RX = rotacion_x(angulo)
print('--Matriz Rotacion X--')
print(matriz_RX)


matriz_RY = rotacion_y(angulo)
print('--Matriz Rotacion Y--')
print(matriz_RY)
print('\n')

matriz_RZ = rotacion_z(angulo)
print('--Matriz Rotacion Z--')
print(matriz_RZ)
print('\n')