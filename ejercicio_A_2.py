#Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos
#matrices previamente inicializadas.

#importar libreria
import numpy as np

#definicion de las matrices
matriz_a = np.array([[1,5,3],[9,6,2],[2,5,8]])
matriz_b = np.array([[8,12,24],[30,65,76],[11,32,8]])

#suma de las mareices
suma = matriz_a+matriz_b
print('suma:', suma)

#resta de las matrices
resta = matriz_a-matriz_b
print('resta:', resta)

#producto matricial ab
producto_matricialab = matriz_a @ matriz_b
print('producto matricial ab:', producto_matricialab)

#producto matricial ba
producto_matricialba = matriz_b @ matriz_a
print('producto matricial ba:', producto_matricialba)

#division de las matrices
 #calculo del determinante de las matrices
determinante_a = np.linalg.det(matriz_a)
determinante_b = np.linalg.det(matriz_b)
 #division de la matriz a entre el determinante de b
division_ab = matriz_a/determinante_b
print('division_ab:', division_ab)
 #division de la matriz b entre el determinante de a   
division_ba = matriz_b/determinante_a
print('division_ba:', division_ba)
