#En python existen 4 tipos de datos elementales (float: numero con coma - int: numero entero - Bool: True, False - string: cadenas de texto)

palabra1 = "Hola "
palabra2 = "Mundo"
print(True * 1)

# operadores numericos: +:suma -:resta *:multiplicar /:divir **:potencia  %:resto de division //:division entera

# operadores logicos: ==:es igual a? !:not or:o and:y !=:es distinto de? <:es
#menor que? <=:es menor o igual que? >: es mayor que? >=: es mayor o igual que?

num = 7
num2 = 4
num3 = 50

#if : si  ,   elif : sino, si    ,   else : sino

if num == num2: #si num1 es igual a num2, entonces:
    print(f'numero 1 {num} y numero 2 {num2} son iguales') #imprimir mensaje
elif num>num2: #sino, si num1 es mayor que num2, entonces:
    print(f'numero 1 {num} es mayor que numero 2 {num2}')
    #print("numero 1",num,"es mayor que numero 2 ",num2)
else: #sino:
    print(f'numero 3 {num3}')

#for:por y while:mientras

for i in range(3): #por i en el rango de 1 a 20 de 2 en 2
    for j in range(3):
        print(f'i:{i} ; j:{j}')

entrada = 99
while entrada != 0: #mientras entrada sea distinto de 0
    entrada = int(input("ingrese un numero por favor: "))
    print(f'Numero es igual a: {num}')
    num += 1 #num = num + 1
    if num == 5:
        raise Exception("NUM NO PUEDE SER MAYOR A 5") #detiene la ejecucion del codigo

entrada = 99
while True: #se ejecuta si o si
    if entrada == 0: #si entrada es igual a 0
        print("adios")
        break
    print("hola")
    entrada = int(input("ingrese un numero por favor: "))

"""

"""