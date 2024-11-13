string1="Lorem ipsum dolor sit amet, dicat dicit dicam est ei. Vim te nonumes corpora, doctus dignissim eos an. Vim no brute audiam omittam. Ea dicit omnium scripta sit."
string2='hola'
string3="""
hola
a 
todos
"""
string4='''

hola
al 
mundo

'''

#print(string1)
#print(string2)
#print(string3)
#print(string4)

print(string1[6]) #devuelve el elemento en la posicion
print(string1[7])
print(string1[8])
print(string1[9])
print(string1[10])

print(string1[6:31]) #devuelve el elemento entre las posiciones 6 y 31
print(string1[:25]) #devuelve todos los elementos hasta la posicion 25
print(string1[-25:]) #devulve todos los elementos hasta la posicion 25 desde el final
print(string1[::-1]) #invierte la cadena

print(len(string2)) #devuelve la cantidad de elementos en la cadena(o lista, arreglo, etc.)

print(string2+''+string3) #concatenacion basica

print(string1.find("dicat")) #devuelve la posicion donde comienze el elemento a buscar

print(string1.find("Ramon")) #devuelve -1 si no existe en el arreglo

print("\n-------------------------------------------------- \n")

print(string1.upper()) #todo mayuscula
print(string1.lower()) #todo minuscula
print(string4.strip()) #elimina espacios en blanco al comienzo y al final

print("\n-------------------------------------------------- \n")

print(string1.replace("Lorem", "albondigas")) #remplaza el primer elemento por el segundo
listaString=string1.split(' ')#separa los elementos del arreglo en base al separador seleccionado
print(listaString)

print("\n-------------------------------------------------- \n")

print('- ;-) -'.join(listaString)) #recorre la lista y crea un string con todos los elementos de esta, junto con el separador

print('.'.join(string2))