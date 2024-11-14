import numpy as np


matriz1 = np.array([[1,2,3],[2,5,4],[3,4,1]])

def escuadrada(matriz):
    filas = matriz.shape[0]
    columnas=matriz.shape[1]
    if filas == columnas:
        return True
    else:
        return False
    
variable=False

for y in range(3):
    for x in range(3):
        if matriz1[y,x] != matriz1[3-y-1, 3-x-1]:
            variable=False
            break
        else:
            variable=True
print(variable)

matriz1= np.zeros((5,5))

for y in range(matriz1.shape[0]):
    for x in range(matriz1.shape[1]):
        if matriz1[y][x] != matriz1[x,y]:
            variable=False
            break
        else:
            variable=True

print(matriz1)
print(variable)