import cv2

#leer primer logo
img1 = cv2.imread(r'C:\Users\lorena\Desktop\robotica\logos\mazda.jpg')
blur1 = cv2.blur(img1, (5, 5)) #filtro para reducir contronos "ruido"
imgCanny1 = cv2.Canny(blur1, 5, 20) #binarizar imagen para detectar los contornos
contorno1, _ = cv2.findContours(imgCanny1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) #realizar contronos eliminando contornos redundantes
cv2.drawContours(img1, contorno1, -1, (0, 255, 0), 2)

#mostrar contronos del primer logo
cv2.imshow('imagen1', img1)
cv2.imshow('canny1', imgCanny1)
print('las coordenadas de los contronos del logo uno son:\n',contorno1)

#leer segundo logo
img2 = cv2.imread(r'C:\Users\lorena\Desktop\robotica\logos\chevrolet.png')
blur2 = cv2.blur(img2, (5, 5))
imgCanny2 = cv2.Canny(blur2, 5, 20)
contorno2, _ = cv2.findContours(imgCanny2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img2, contorno2, -1, (0, 255, 0), 2)

#mostrar contornos del segundo logo 
cv2.imshow('imagen2', img2)
cv2.imshow('canny2', imgCanny2)
print('las coordenadas de los contronos del logo uno son:\n',contorno2)

cv2.waitKey(0)
cv2.destroyAllWindows()
