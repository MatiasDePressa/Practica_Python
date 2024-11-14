import numpy as np
vector1 = np.array([1,2,3,4,5,6])
print(vector1)

def modifica_pares(vector):
    for i in range(len(vector)):
        if i % 2 == 0:
            vector[i] = 56
    return vector

#def espar(valor):
#    return valor % 2 == 0

print(modifica_pares(vector1))

def eliminar(vector, posicion):
    if posicion>=len(vector):
        raise Exception("posicion invalida")
    else:
        vector[posicion] = 0
    return vector

print(eliminar(vector1, 3))
print(len(vector1))
#vector2 = np.zeros(len(vector1))
#print(vector2)

def agregar(vector, producto):
    vector2 = np.zeros(len(vector)+1)
    for i in range(len(vector)):
        vector2[i] = vector[i]
    vector2[len(vector)] = producto
    return vector2

vector3 = np.empty(3, dtype='<U55')
vector3[2]="camisa"
print(vector3)

vector1 = agregar(vector1, 75)
print(vector1)