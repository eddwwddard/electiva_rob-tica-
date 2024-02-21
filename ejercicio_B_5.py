#Escribir un programa que realice la pregunta ¿Desea continuar Si/No? y que no deje de hacerla
#hasta que el usuario teclee No.

while True:
    #preguntar al usuario si desea continuar
    respuesta = input("¿Desea continuar? (si/no): ").lower()

    #verificar la accion que se realiza segun la respuesta del usuario
    if respuesta == 'si':
        respuesta = input("¿Desea continuar? (si/no): ").lower()
    elif respuesta == 'no':
        break
    else:
    #confrimar que la respuesta del usuario sea si o no
        print("Por favor, ingresa 'si' o 'no'.")