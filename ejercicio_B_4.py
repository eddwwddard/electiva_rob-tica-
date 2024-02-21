#Realice un programa que le permita al usuario escoger entre robot Cilíndrico, Cartesiano y esférico,
#donde como respuesta a la selección conteste con el tipo y número de articulaciones que posee.

#importar libreria
import numpy as np

#funciones con la descricion de las articulaciones segun el tipo de motor
def cilindrico():
    print("el robot cilindrico tiene tres articulaciones \n una rotacional para la base \n una prismatica para la altura \n una prismatica para el radio ")
def carteciano():
    print("el robot cartecioano tiene tres articulaciones prismaticas para desplazarce en los ejes X,Y y Z") 
def esferico():
    print("el robot esferico tiene tres articulaciones rotacionales para realizar dezplamientos y cambios en la orientacion del efector final")

# variable para llamar la funcion correspondiente al robot deseado
opciones = {
    '1': cilindrico,
    '2': carteciano,
    '3': esferico,
} 
 
#ciclo para desplegar el menu de opciones y seleccionar la deseada
while True: 
    print("\nSeleccione el robot del que desea saber sus articulaciones: ")
    print("1. cilindrico")
    print("2. carteciano")
    print("3. esferico")

    opcion = input("Ingrese el numero de la opción que desea: ")
   
    if opcion in opciones:
        opciones[opcion]()
    else:
        print("Opción no válida. Por favor, ingresa un número del 1 al 3.")      