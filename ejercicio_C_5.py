print('\nPUNTO 5-C')
print('Dibuje el nombre de cada uno de los integrantes del grupo en un plot en 2D, teniendo en cuenta líneas rectas y/o curvas.\n')


import matplotlib.pyplot as plot

#Coordenadas de los puntos 
Coordenadas = {

'O':[(1, 2), (2, 3), (3, 2), (2, 1), (1, 2)],
'M':[(4, 1), (4, 3), (5, 2), (6, 3), (6, 1)],
'A':[(7, 1), (9, 3), (10, 2), (8, 2), (10, 2),(11,1)],
'R':[(12, 1), (12, 3), (13, 3), (14, 2), (12, 2), (14, 1)],

}

CoordenadasE={

'E':[(3, 3), (1, 3), (1, 2), (3, 2), (1, 2),(1, 1),(3, 1)],#'E':[(3, 3), (1, 3), (2, 3), (1, 3), (1, 1),(3, 1)],
'D':[(4, 3), (4, 1), (6, 2), (4, 3)],
'W':[(6.5, 3), (7.5, 1), (8.5, 3), (9.5, 1), (10.5, 3)],
'A':[(11, 1), (13, 3), (14, 2), (12, 2), (14, 2),(15,1)],
'R':[(16, 1), (16, 3), (17, 3), (18, 2), (16, 2), (18, 1)],
'D2':[(19, 3), (19, 1), (21, 2), (19, 3)],

}
#Cear PLOT
plot.figure(figsize=(8, 6))

# Dibujar líneas rectas o curvas para cada letra del nombre "OMAR"
for letra, puntos in Coordenadas.items():
    x_coords = [coord[0] for coord in puntos]
    y_coords = [coord[1] for coord in puntos]
    plot.plot(x_coords, y_coords, marker='o', label=letra)

#dibujar rectas
plot.title('Nombres OMAR EDWARD en un plot ')
plot.xlabel('Coordenada X')
plot.ylabel('Coordenada Y')


plot.legend() #para identificar etiquetqas 

# Mostrar el plot
plot.grid(True)  #activa cuadricula 
plot.tight_layout()  # para justar automaticamnte los que se va a imprimir
plot.show() #se utiliza para mostrar el plot en la pantalla 

#Cear PLOT
plot.figure(figsize=(8, 6))

    # Dibujar líneas rectas o curvas para cada letra del nombre EDWAR"
for letra, puntos in CoordenadasE.items():
    x_coords = [coord[0] for coord in puntos]
    y_coords = [coord[1] for coord in puntos]
    plot.plot(x_coords, y_coords, marker='o', label=letra)

#dibujar rectas
plot.title('Nombres EDWARD en un plot ')
plot.xlabel('Coordenada X')
plot.ylabel('Coordenada Y')    

# Mostrar el plot
plot.grid(True)
plot.tight_layout()
plot.show()