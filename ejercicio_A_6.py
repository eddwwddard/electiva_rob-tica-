#Realice un programa que calcule la fuerza de avance y retroceso de un cilindro neumático de doble
#efecto. Debe establecer previamente los valores de presión, así como las dimensiones físicas del
#cilindro para realizar el cálculo.

#importar libreria
import numpy as np
presion = 600000   #presion de trabajo 6 bar ---> 600000 Pa
diam_vast = 0.025  #diametro del vatago 25 mm ---> 0.025 m
diam_embo = 0.1    #diametro del embolo 100 mm ---> 0.1 m

area_vast = (np.pi*(diam_vast**2))/4 #calculo del area del vastago
area_embo = (np.pi*(diam_embo**2))/4 #calculo del area del embolo

#fuerza de avance
F_av = presion*area_embo  
print('la fuerza de avance del cilindro es: \n', format (F_av, ".2f"), 'N')

#fuerza de retroceso
F_ret = presion*(area_embo-area_vast) 
print('la fuerza de retroceso del cilindro es: \n', format (F_ret, ".2f"), 'N')
