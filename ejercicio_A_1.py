import numpy as nupi #importamos biblioteca NumPy como asignacion np 

# en lugar de escribir numpy.array() podmeos escribir np.array()
#NumPy es una de las bibliotecas más utilizadas en Python para realizar operaciones numéricas y matriciales de manera eficiente. 
print('\nPUNTO 1-A')
print('1. Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos vectores previamente inicializados.\n')
   
#Defino vectores
Array1 = nupi.array([9, 5, 1])  
Array2 = nupi.array([8, 4, 2])

#vector_a = np.array([9,5,1,3,7])
#vector_b = np.array([8,4,2,6,0])

#Imprimimos vectores
print('Inicializacion de vectores:')
print(Array1)
print(Array2)
print('\n')

#Suma +  
Suma_A = (Array1 + Array2)
print('Suma (+):' , Suma_A)

#Resta -
Resta_B = Array1 - Array2
print('Resta (-):' ,Resta_B)

#punto producto
ProductoP = nupi.dot(Array1,Array2)             #nupi.dot: Calcula el  producto punto de dos vectores
print('Producto punto (.): ',ProductoP)

#producto cruz 
ProductoC  = nupi.cross(Array1,Array2)        #nupi.cross: Calcular producto cruz 
print('Producto cruz (X): ', ProductoC)

#division de vectores 
Division_c = Array1/Array2
print('Division (/): ', Division_c) 

print('\n')