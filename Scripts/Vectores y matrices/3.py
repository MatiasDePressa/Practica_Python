import numpy as np

vector="hola"
def eliminarletra(long,vector,letra,suma,cont):
    if long==0:
        return suma
    else:
        if vector[long-1]==letra:
           
            return eliminarletra(long-1,vector,letra,suma,cont)
        else:
            cont+=1
            suma+=vector[long-1]
            print(cont)
            return eliminarletra(long-1,vector,letra,suma,cont)
    if cont-1 ==len(vector):
        raise Exception
    print(vector)

eliminarletra(len(vector),vector,"o","",0)

