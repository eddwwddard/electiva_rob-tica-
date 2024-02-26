#Realice un programa que grafique el comportamiento de un sensor PT100 desde -200°C a 200°C.

import matplotlib.pyplot as plt #libreria para realizar graficos
import numpy as np 

#formula de una PT100 modelo de callendar y van dusen para reangos de -200°C a 650°C
#R(T)=R(0)(1+aT+bT^2)
#R(0)=resistencia del sensor a 0°C
#a,b=coeficiente de callendar y dusen del cambio del sensor con la temperatura 
#parametros de la ecuacion de la PT100

R= 100
A= 3.9083e-3
B= -5.775e-7
C= -4.183e-12


#definicion del rango de temperatura -200°C a 200°
T = np.linspace(-200, 200, 1000)

#ecucacion de resistencia de la PT100
# Función para calcular la resistencia en función de la temperatura
def resistance(T):
    if T >= 0:
       return  R*(1+(A*T)+(B*(T**2)))
    else:
        return R*(1+(A*T)+(B*(T**2))+(C*((T-100)*T**3)))

# Calcular la resistencia para cada temperatura en el rango dado
res = np.array([resistance(temp) for temp in T])

#grafica de ressitencia vs temperatura
plt.plot(T,res)
plt.title ('comportamiento de la PT100')
plt.xlabel('temperatura °C')
plt.ylabel('resistencia ohms')
plt.grid (True)
plt.show()
