#Realice un programa para el cálculo de la resistencia de una RTD de platino (PT100) en función de
#la temperatura.

print('\nPUNTO 4-A')
print('Realice un programa para el cálculo de la resistencia de una RTD de platino (PT100) en función de la temperatura.\n')


#coeficiente para un PT100
R= 100
A= 3.9083e-3
B= -5.775e-7
C= -4.183e-12



# Colocamos una temperatura en ceslius
T = 173           


# Calcular la resistencia en función de la temperatura
if T >= 0:
    resistencia = R*(1+(A*T)+(B*(T**2)))
else:
    resistencia = R*(1+(A*T)+(B*(T**2))+(C*((T-100)*T**3)))
#Imprimo resultado 
print('Para una temperatura de 25 Celsius la resistencia es:' ,resistencia,'OHMIOS')