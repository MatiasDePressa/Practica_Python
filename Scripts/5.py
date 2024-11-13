#seleccionar entre un circulo y un cuadrado, y calcular el perimetro y el area de cada figura (si es un cuadrado se calcula dado su base y altura)

def calcularCuadrado(base, altura): 
    # se crea una funcion que toma la base  y la altura de un cuadrado o rectangulo
    # y se retornan los resultados de los calculos respectivos del perimetro y del area 
    perimetro = 2 * (base + altura)
    area = base * altura
    return perimetro, area

def calcularCirculo(radio):
    # se crea una funcion que toma el radio de un circulo y se retornan los resultados de los calculos respectivos del perimetro y del area
    perimetro = 2 * 3.1415 * radio
    area = 3.1415 * (radio ** 2)
    return perimetro, area

def calcularFigura(figura, base=None, altura=None):
    # se pide una figura y, en caso de que sea un circulo, un parametro mas
    # o en caso de que sea un cuadrado, dos parametros mas
    # para evitar errores, se igualan ambos a None
    if figura.lower() == "cuadrado":
        #verificamos que sea un cuadradado y realizamos la verificacio en minuscula
        try:
            #verificamos que los parametros no tengan ningun tipo de error, si no lo tienen almacenamos el perimetro y el area en variables
            perimetro, area = calcularCuadrado(base, altura)
            #retornamos un diccionario con los datos
            return {"figura": "cuadrado", "perimetro": perimetro, "area": area}
        except:
            #en caso de tener error, detener la ejecucion
            raise Exception("Se necesita una base y una altura")
        
    elif figura.lower() == "circulo":
        #verificamos que sea un cuadradado y realizamos la verificacio en minuscula
        try:
            #verificamos que los parametros no tengan ningun tipo de error, si no lo tienen almacenamos el perimetro y el area en variables
            perimetro, area = calcularCirculo(base)
            #retornamos un diccionario con los datos
            return {"figura": "circulo", "perimetro": perimetro, "area": area}
        except:
            #en caso de tener error, detener la ejecucion
            raise Exception("Se necesita un radio, palurdo")
        
    else:
        #en caso de que no se haya seleccionado una figura valida, detener la ejecucion
        raise Exception("Persona de bajo coeficiente intelectual, seleccionar un cuadrado o un circulo")

resutado_circulo = calcularFigura("circulo", 3)
resutado_cuadrado = calcularFigura("cuadrado", 4, 6)

print(resutado_circulo)
print(resutado_cuadrado)