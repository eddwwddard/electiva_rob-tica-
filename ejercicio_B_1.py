#Realice un programa que calcule la potencia que consume un circuito ingresando por teclado el
#valor de corriente y voltaje.

#ciclo while para rechazar el ingreso de valores diferentes a numeros
while True:     
    try:
        A = float(input("Ingrese el valor de la corriente consume el circuito en amperios (A): \n")) #solicitud de la corriente
        break 
    except ValueError:
        print("ingrese un número válido") #rechazo de valores errados

#ciclo while para rechazar el ingreso de valores diferentes a numeros
while True:
    try:
        V = float(input("Ingrese el valor del votaje de alimentacion del circuito en voltios (V): \n")) #solicitud de la tensión
        break 
    except ValueError:
        print("ingrese un número válido") #rechazo de valores errados

W=A*V #calculo de la potencia consumida por el circuito

print('la potencia que consume el circuito en vatios (W) es: \n', W) 
