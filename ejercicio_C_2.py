#importar librerias
import control #libreria para control
import matplotlib.pyplot as plt #libreria para graficar
import numpy as np
num = [float(x) for x in input('ingrese los coeficientes del numerador separados por un espacio: ').split()] #instruccion para ingresar los datos del numerador y recorrer los puntos de tiempo y las respuestas del sistema
den = [float(x) for x in input('ingrese los coeficientes del denominador separados por un espacio: ').split()] #instruccion para ingresar los datos del denominador y recorrer los puntos de tiempo y las respuestas del sistema

if len(den) != 3:
    print("la funcion de transferencia debe de ser de segundo orden ejecute nuevamente el programa")
    exit()

#funcion de transferencia
G = control.TransferFunction(num,den)
#respuesta temporal
t,y=control.step_response(G)

#grafica de la respuesta temporal
plt.plot(t,y)
plt.xlabel('tiempo s')
plt.ylabel('respuesta')
plt.title('respuesta temporal al escalon unitario')


#tipo de sistema
if np.iscomplex(y).any():   #verificacionde polos complejos puros
    tipo = 'subamortiguado'
elif np.allclose(y[-1],0):  #comprobacion de los valores de y para determinar si tienden a cero sin oscilacion
    tipo = 'criticamente amortiguado'
else:
    tipo = 'amortiguado'  #caso en el cual el sistema tiende a cero pero con oscilaciones previas 

plt.text(0.1, 0.9, f'tipo de sistema:{tipo}', transform = plt.gca().transAxes) #escribir sobre la grafica el tipo de sistema usando como referencia los ejes coordenados del grafico actual

plt.grid()

#grafica del sistema
plt.show()