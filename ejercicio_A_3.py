#Realice un programa que convierta coordenadas rectangulares a cilíndricas y esféricas, para lo cual
# deben consultar sobre el uso de funciones trigonométricas en Python.

#importar libreria
import numpy as np

# definicion del vector de coordenadas rectangulares
cord_rec = np.array([9, 12, 10])
print('coordenadas rectangulares: ', cord_rec)

#conversion de las coordenadas rectangulares a esfericas (rho, theta, phi)
 #calculo de rho
rho = np.sqrt((9**2)+(12**2)+(10**2))
 #calculo de theta
theta = np.arccos(10/rho)
 #calculo de phi
phi = np.arctan(12/9)

#coordenadas esfericas
print("Coordenadas esféricas: ")
print("Radio (rho):", rho)
#convertir theta a grados
print("Ángulo polar (theta):", np.degrees(theta)) 
#convertir phi a grados 
print("Ángulo azimutal (phi):", np.degrees(phi))  