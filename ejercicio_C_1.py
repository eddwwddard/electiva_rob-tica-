#Realice un programa que grafique el comportamiento de un sensor PT100 desde -200°C a 200°C.

import matplotlib.pyplot as plt #libreria para realizar graficos
import numpy as np 

#formula de una PT100 modelo de callendar y van dusen para reangos de -200°C a 650°C
#R(T)=R(0)(1+aT+bT^2)
#R(0)=resistencia del sensor a 0°C
#a,b=coeficiente de callendar y dusen del cambio del sensor con la temperatura 
#parametros de la ecuacion de la PT100

a = 3.9083e-3 # ohm/(ohm*°C) IEC 60751
b = -5.775e-7 # ohm/(ohm*°C) IEC 60751
R0 = 100 # ohm segun IEC 60751

#definicion del rango de temperatura -200°C a 200°
tem = np.linspace(-200, 200, 1000)

#ecucacion de resistencia de la PT100
res = R0*(1+a*tem+b*tem**2)

#grafica de ressitencia vs temperatura
plt.plot(tem,res)
plt.title ('comportamiento de la PT100')
plt.xlabel('temperatura °C')
plt.ylabel('resistencia ohms')
plt.grid (True)
plt.show()
