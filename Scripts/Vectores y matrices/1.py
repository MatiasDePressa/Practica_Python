import numpy as np

matriz = np.array([[1,2,3,78],[4,5,6,98],[7,8,9,34]])
print(matriz)
matriz1 = np.zeros((3,3))
print(matriz1)

print(matriz.shape)
print(len(matriz))
print(matriz.size)
print("\n --------------------<>-------------------\n")


matriz2 = np.array([[1,2],[3,4]])
matriz3 = np.array([[4,3],[2,1]])

matriz4 = matriz2 % matriz3
print(matriz4)

matriz4 = matriz4 - 4
print(matriz4)

print("\n --------------------<>-------------------\n")
print("Shape")

print(f'cantidad de filas(y): {matriz.shape[0]}')
print(f'cantidad de columnas(x): {matriz.shape[1]}')

print("\n --------------------<>-------------------\n")

matriz5 = np.zeros((9,9))

for y in range(matriz5.shape[0]):
    for x in range(matriz5.shape[1]):
        matriz5[y,x] = y+x

print(matriz5)

matriz6 = np.empty((3,3), dtype=object)

for y in range(matriz6.shape[0]):
    for x in range(matriz6.shape[1]):
        matriz6[y,x] = (y,x)

print(matriz6)

print("\n --------------------<>-------------------\n")


