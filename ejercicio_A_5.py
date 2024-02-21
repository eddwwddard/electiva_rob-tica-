#Realice en funciones las rotaciones en X, Y y Z, donde se tenga un parámetro de entrada (ángulo)
#y un parámetro de salida (matriz).

#importar libreria 
import numpy as np

#funcion para realizar la rotacion en X
def rotacion_x(matriz, angulo):
    rad_angulo = np.radians(angulo)  #conversion del angulo de grados a radianes
    matriz_de_rotacion = np.array([[1,0,0],[0,np.cos(rad_angulo),-np.sin(rad_angulo)],
                                   [0,np.sin(rad_angulo),np.cos(rad_angulo)]]) #matriz de rotacion en el eje X
    matriz_rotada = np.dot(matriz, matriz_de_rotacion)
    return(matriz_rotada)

#funcion para realizar la rotacion en Y
def rotacion_y(matriz, angulo):
    rad_angulo = np.radians(angulo)  #conversion del angulo de grados a radianes
    matriz_de_rotacion = np.array([[np.cos(rad_angulo),0,np.sin(rad_angulo)],[0,1,0],
                                   [-np.sin(rad_angulo),0,np.cos(rad_angulo)]]) #matriz de rotacion en el eje Y
    matriz_rotada = np.dot(matriz, matriz_de_rotacion)
    return(matriz_rotada)

#funcion para realizar la rotacion en Z
def rotacion_z(matriz, angulo):
    rad_angulo = np.radians(angulo)  #conversion del angulo de grados a radianes
    matriz_de_rotacion = np.array([[np.cos(rad_angulo),-np.sin(rad_angulo),0],[np.sin(rad_angulo),np.cos(rad_angulo),0],
                                   [0,0,1]]) #matriz de rotacion en el eje Z
    matriz_rotada = np.dot(matriz, matriz_de_rotacion)
    return(matriz_rotada)

matriz = np.array([[1,5,3],[2,8,9],[0,7,3]]) #matriz que se quiere rotar
angl=45 #angulo de rotacion de la matriz

#matriz rotada en x
rotada_x=rotacion_x(matriz,angl)
print('la matriz rotada en el eje X con un angulo de ',angl,'° es:\n',rotada_x)

#matriz rotada en y
rotada_y=rotacion_y(matriz,angl)
print('la matriz rotada en el eje Y con un angulo de ',angl,'° es:\n',rotada_y)

#matriz rotada en z
rotada_z=rotacion_z(matriz,angl)
print('la matriz rotada en el eje Z con un angulo de ',angl,'° es:\n',rotada_z)
