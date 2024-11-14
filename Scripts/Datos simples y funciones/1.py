#Escribir un Programa que realice la transformacion de grados Celsius a Fahrenheit

def pasoDeCelsiusAFahrenheit(temperatura):
    try:#en caso de que la temperatura sea un numero
        return float((temperatura*(9/5))+32) #retornar la formula del traspaso
    except:#en caso de que la temperatura no sea un numero
        raise Exception("La temperatura debe de ser un numero")
        #retornar una excepcion

print(pasoDeCelsiusAFahrenheit(33))