#Importo librerias
import numpy as np
import random

#inicializo las variables
print("La cantidad minima de funciones es una sola y la maxima cantidad son 10 funciones")
n = int(input("Ingresar la cantidad de funciones: "))
print("\n")
cont=0
sumapromtotal=0
sumaxfun=0
funnum=0

#analizo que la cantidad de funciones sea la correspondiente y creo la matriz
if n<1 or n>10:
    raise Exception("la cantidad de funciones no es la correspondiente")
sala = np.zeros([3,n],int)

#lleno la matriz de numeros aleatorios de entre 50 y 300
for funcion in range(3):
    for turno in range(n):
        sala[funcion][turno]=random.randint(50,300)
print(sala)
print("\n")

#saco el promedio de entradas vendidas en total
for funcion in range(3):
    for turno in range(n):
        sumapromtotal += sala[funcion][turno]
        cont += 1
print("El promedio de entradas vendidas en total es:",round(sumapromtotal/cont,0))
print("\n")

#saco la cantidad de entradas vendidas en cada funcion
for turno in range(n):
    for funcion in range(3):
        sumaxfun += sala[funcion][turno]
    funnum +=1
    print("la cantidad de entradas vendidas en la funcion n°",funnum,"es:",sumaxfun)
    sumaxfun = 0