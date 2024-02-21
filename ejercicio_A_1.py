#Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos
# vectores previamente inicializados.

#importar libreria
import numpy as np

#definicion de los vectores
vector_a = np.array([9,5,1,3,7])
vector_b = np.array([8,4,2,6,0])

#suma de los vectores
suma = vector_a+vector_b
print('suma:', suma)

#resta de los vectores
resta = vector_a-vector_b
print('resta:', resta)

#producto cruz de los vectores
producto_cruz = vector_a*vector_b
print('producto cruz:', producto_cruz)

#producto punto de los vectores
producto_punto = vector_a @ vector_b
print('producto punto:', producto_punto)

#division de los vectores
 #calculo de la norma de los vectores
norma_a = np.linalg.norm(vector_a)
norma_b = np.linalg.norm(vector_b)
 #division del vector a entre la norma de b
division_ab = vector_a/norma_b
print('division_ab:', division_ab)
 #division del vector b entre la norma de a   
division_ba = vector_b/norma_a
print('division_ba:', division_ba)
