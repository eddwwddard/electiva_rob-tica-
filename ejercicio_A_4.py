#Realice un programa para el cálculo de la resistencia de una RTD de platino (PT100) en función de
#la temperatura.
#formula de una PT100
#R(T)=R(0)(1+aT)
#R(0)=resistencia del sensor a 0°C
#a=coeficiente del cambio del sensor con la temperatura 

R0=100    # ohm segun IEC 60751
a=0.00385 # ohm/(ohm*°C) IEC 60751

#funcion para hallar el valor de la resistencia
def res_tem(T):
    Rt=R0*(1+(a*T))
    return Rt

#variable de temperatura
T=110
#resultado de la funcion
Rt=res_tem(T)
#valor de resistencia en funcion de temperatura en una PT1100
print('la resitencia de una PT100 a ',T,'°C es de:',Rt,'ohm')

