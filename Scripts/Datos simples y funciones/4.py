def Saludar():
    #print("hola")
    return "Mundo"

palabra = Saludar()
print(palabra)
print(Saludar())

def SaludarAlguien(nombre="Maria"):
    def Caminar():
        print(f'{nombre.upper()} camino 50 pasos')

    Caminar()
    return "hola "+nombre

#nombre1= str(input("Ingrese su nombre por favor: "))
print(SaludarAlguien("maria"))

def Sumar(*numero:int) -> int:
    return sum(numero)
    #suma = 0
    #for num in numero:
    #    suma += num
    #return suma

print(Sumar(1,2,3,4,5,6,7))

suma = lambda a,b: a+b
print(suma(2,4))


# Estructuras de datos: Listas, Tuplas, Set, diccionarios
lista = [1,2,3,4,5,"hols",4.56,True]
print(lista)
for i in lista:
    print(i)

lista.append(97)
print(lista)
lista.remove(4.56)
print(lista)
lista.pop(2)
print(lista)
lista.reverse()
print(lista)
#
#lista2 = []
#for i in range(10):
#    lista2.append(input("ingrese un dato: "))

#print(lista2)

tupla = (1,2,3,"hola")
print(tupla[3])

sett = {1,2,5645,456,234,5645}
#print(sett[5])

dictionary = {
            'nombre':['Matias', 'noelia'],
            'edad':[19, 21],
            'profecion':['profe', 'constructora']
            }

print(dictionary)

def AgregarPersona(dictionary:dict):
    for i in dictionary.keys():
        dictionary[i].append(input(f'coloque el o la {i} de una persona: '))
    return dictionary

dictio = AgregarPersona(dictionary)
print(dictio)

#print(dictionary['nombre'].append('jorge'))
#
#print(dictionary)

