#importar librerias
import control #libreria para control
import matplotlib.pyplot as plt #libreria para graficar
import numpy as np
#ingresar valores de la funcion de transferencia frecuencia natural, factor de amortiguamiento y ganancia
gain=float(input("ingrese el valor de la ganancia: "))
Wn=float(input("ingrese el valor de la frecuencia natural: "))
z=float(input("ingrese el factor de amortiguamiento: "))

num = [(gain*(Wn**2))]
den = [1,(2*z*Wn),(Wn**2)]

#if len(den) != 3:
#print("la funcion de transferencia debe de ser de segundo orden ejecute nuevamente el programa")
#exit()

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
if z==0:
    tipo='oscilador puro'
    print(tipo)
if 0<z and z<1:
    tipo='subamoriguado'
    print(tipo) 
if z==1:
    tipo='criticamente amortiguado'
    print(tipo)
if z>1:
    tipo='sobreamortiguado'
    print(tipo)
if z<0:   
    tipo='inestable'
    print(tipo)

       
plt.text(0.1, 0.9, f'tipo de sistema:{tipo}', transform = plt.gca().transAxes) #escribir sobre la grafica el tipo de sistema usando como referencia los ejes coordenados del grafico actual

plt.grid()

#grafica del sistema
plt.show()