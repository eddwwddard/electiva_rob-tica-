#Realice un programa para el cálculo de volúmenes (Prisma, Pirámide, Cono truncado, Cilindro)
#donde el usuario pueda seleccionar el sólido y los parámetros de cada volumen.

#importar libreria
import numpy as np

#funcion para calcular el volumen de un prisma rectangular
def prisma():
    print('volumen del prisma:\n')
    while True: #ciclo para evitar que se ingresen valores inadecuados
        try:    
            h = float(input('ingrese la altura del prisma:\n'))
            la = float(input('ingrese el lado A:\n'))
            lb = float(input('ingrese el lado b:\n'))
            break
        except ValueError:
            print('ingrese un valor numerico \n')
    vol = la*lb*h #ecuacion del volumen del prisma rectangular
    print('el volumen del prisma es: \n', vol)

#funcion para calcular el volumen de una priamide de base cuadrada
def piramide():
    print('volumen de la piramide:\n') 
    while True: #ciclo para evitar que se ingresen valores inadecuados
        try:
            l = float(input('ingrese el valor de los lados:\n'))
            h = float(input('ingrese el valor de la altura: \n'))
            break
        except ValueError:
            print('ingrese un valor numerico \n')
    vol_p = ((l**2)*h)/3 #ecuacion del volumen de una piramide de base cuadrada  
    print('el volumen de la piramide es: \n',vol_p)

#funcion para calcular el volumen de un cono truncado
def cono_trun():
    print('volumen del cono truncado: \n')
    while True:  #ciclo para evitar que se ingresen valores inadecuados
        try:
            Rad_bma = float(input('ingrese el valor del radio de la base mayor:\n'))
            Rad_bme = float(input('ingrese el valor del radio de la baser menor:\n'))
            h = float(input('ingrese el valor de la altura:\n'))
            break
        except ValueError:
            print('ingrese un valor numerico \n')
    vol = (((1/3)*np.pi*h*(Rad_bma**2+Rad_bme+Rad_bma*Rad_bme))) #ecuacion del volumen de un cono truncado
    print('el volumen del cono truncado es:\n', vol)
#funcion para calcular el volumen de un cilindro
def cilindro():
    print('volumen del cilindro: \n')
    while True:  #ciclo para evitar que se ingresen valores inadecuados
        try:
            rad = float(input('ingrese el valor del radio:\n'))
            h = float(input('ingrese el valor de la altura:\n'))
            break
        except ValueError:
            print('ingrese un valor nuerico \n')
    vol = (np.pi*(rad**2)*h) #ecuacion del volumen de un cilindro
    print('el volumen del cilindro es: \n',vol)


# variable para llamar la funcion correspondiente al volumen deseado
opciones = {
    '1': prisma,
    '2': piramide,
    '3': cono_trun,
    '4': cilindro
}
#ciclo para desplegar el menu de opciones y seleccionar la deseada
while True: 
    print("\nSeleccione la forma de la cual desea saber su volumen:")
    print("1. prisma")
    print("2. piramide")
    print("3. cono truncado")
    print("4. cilindro")

    opcion = input("Ingrese el numero de la opción que desea: ")
   
    if opcion in opciones:
        opciones[opcion]()
    else:
        print("Opción no válida. Por favor, ingresa un número del 1 al 4.")