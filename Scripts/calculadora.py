import json
import math
import time

fileName='resultados.json'

def GuardarResultado(operacion, resultado):
    horario = time.strftime('%Y-%m-%d %H:%M:%S')

    entrada = {
        'operacion':operacion,
        'resultado':resultado,
        'hora':horario
    }

    try:
        with open(fileName,'r') as i:
            contenido = i.read().strip()
            if contenido:
                datos= json.loads(contenido)
            else:
                datos=[]
    except FileNotFoundError:
        datos = []

    datos.append(entrada)
    with open(fileName, 'w') as i:
        json.dump(datos, i, indent=4)


def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if a==0 or b==0:
        return "No se puede dividir por 0"
    return a / b

def raiz(a):
    return math.sqrt(a)

def potenciar(a,b):
    #math.pow(a,b)
    return a ** b

def menu():
    with open('menu.txt','r', encoding='utf-8') as archivo:#abro el archivo y lo recorro en modo lectura
        contenido = archivo.read()
    print(contenido)

def calculadora():
    while True:
        menu()
        opcion=int(input("Elija una operacion (0 para salir): "))

        if opcion==0:
            print("Saliendo...")
            break

        elif opcion>=1 and opcion<=5:

            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))

            if opcion == 1:
                resultado = sumar(a,b)
                operacion = f'{a}+{b}'
            elif opcion == 2:
                resultado = restar(a,b)
                operacion = f'{a}-{b}'
            elif opcion == 3:
                resultado = multiplicar(a,b)
                operacion = f'{a}*{b}'
            elif opcion == 4:
                resultado = dividir(a,b)
                operacion = f'{a}/{b}'
            elif opcion == 5:
                resultado = potenciar(a,b)
                operacion = f'{a}^{b}'
        
        elif opcion==6:
            a = float(input("Ingrese un numero: "))
            resultado=raiz(a)
            operacion=f'Raiz Cuadrada({a})'

        else:
            print("Ingrese una opcion valida")
            continue

        print(f'Resultado: {resultado}')
        GuardarResultado(operacion, resultado)

calculadora()    