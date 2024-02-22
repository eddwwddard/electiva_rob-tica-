print('\nPUNTO 4-C')
print('Consulte y elabore un sistema coordenado X, Y y Z donde se dibuje un vector con coordenadas ingresadas por el usuario.\n')

import matplotlib.pyplot as plt    #interfaz grafica 
from mpl_toolkits.mplot3d import Axes3D  #para graficos tridimensionales

# insertar coordenadas em XYZ
X = float(input('Ingresar la coordenada en X : '))
Y = float(input('Ingresar la coordenada en Y : '))
Z = float(input('Ingresar la coordenada en Z : '))

# Crear una figura 3D
fig = plt.figure()     #crea una nueva figura vacia
ax = fig.add_subplot(111, projection='3d') # Esta línea agrega un nuevo subplot (subgráfico) a la figura creada anteriormente
# El argumento 111 indica que queremos un solo subplot en una cuadrícula de 1x1, y projection='3d' especifica que queremos un subplot en 3D.

#Dibujar el sistmea de coordenadas
#ax.quiver() se utiliza para dibujar una flecha en un gráfico 
ax.quiver(0, 0, 0, 1, 0, 0, color='r', label='X')
ax.quiver(0, 0, 0, 0, 1, 0, color='g', label='Y')
ax.quiver(0, 0, 0, 0, 0, 1, color='b', label='Z')

# Dibujar el vector ingresado por el usuario
ax.quiver(0, 0, 0, X, Y, Z, color='yellow', label='Vector')

# Ajustar los limites de los ejes 
max_range = max(X,Y,Z)
ax.set_xlim([-max_range, max_range])
ax.set_ylim([-max_range, max_range])
ax.set_zlim([-max_range, max_range])

# Añadir etiquetas y leyenda
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Mostrar el plot
plt.title('VECTOR : sistema de coordenadas 3D')
plt.show()