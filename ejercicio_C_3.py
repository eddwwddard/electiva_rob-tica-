import numpy as np 
import matplotlib.pyplot as plt

#Ingrese datos de valores voltaje capacitancia resistencia 
Vo = float(input('Digite el VOLTAJE:'))
Ca = float(input('Digite CAPACITOR:'))
Re = float(input('Digite la RESISTENCIA: '))

#calcular Tao
T = Re*Ca

#calculo de timepo para la grafica 
tiempo = np.linspace(0, 5*T, 1000)
# np.linspace() crea un array de números 
# es el numero de puntos que se generan en el array

#calculo de voltaje de carga del capacitr
Voltaje_C = Vo *(1- np.exp( -tiempo/ T))

#calculo de voltaje de descarga
Voltaje_D = Vo * np.exp(-tiempo / T)

# Graficar la carga y descarga del capacitor
plt.figure(figsize=(10, 6))
plt.plot(tiempo, Voltaje_C, label='CARGA CAPACITOR')
plt.plot(tiempo, Voltaje_D, label='DESCARGA CAPACITOR')
plt.title('CARGA Y DESCARGA CIRCUITO RC')
plt.xlabel('Tiempo')
plt.ylabel('Voltaje')
plt.legend()
plt.grid(True)
plt.show()