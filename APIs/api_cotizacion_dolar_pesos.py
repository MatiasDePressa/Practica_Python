import requests
import json

with open('key_api_pesos.json', 'r') as file:
    data = json.load(file)
    api_key = data['api_key']

url = f'https://magicloops.dev/api/loop/{api_key}/run'

response = requests.get(url)
responseJson = response.json()

compra_dolares = float(responseJson['USD_to_ARS']['compra'])
venta_dolares = float(responseJson['USD_to_ARS']['venta'])

compra_pesos = float(responseJson['ARS_to_USD']['compra'])
venta_pesos = float(responseJson['ARS_to_USD']['venta'])

while True:
    tipo_moneda = input("ingrese el tipo de moneda que desea cambiar (dolar o pesos): ")

    try:
        cantidad_a_cambiar = float(input("ingrese un cantidad de monedas que desea cambiar: "))
    except ValueError:
        print("seleccione una opcion valida para la cantidad")
        continue

    tipo_operacion = input("ingrese el tipo de operacion que desea ejecutar (venta o compra): ")

    if tipo_moneda.lower() == "dolar":
        if tipo_operacion.lower() == "compra":
            print(compra_dolares * cantidad_a_cambiar)
        elif tipo_operacion.lower() == "venta":
            print(venta_dolares * cantidad_a_cambiar)
        else:
            print("seleccione una opcion valida para la operacion")

    elif tipo_moneda.lower() == "pesos":
        if tipo_operacion.lower() == "compra":
            print(compra_pesos * cantidad_a_cambiar)
        elif tipo_operacion.lower() == "venta":
            print(venta_pesos * cantidad_a_cambiar)
        else:
            print("seleccione una opcion valida para la operacion")
    else:
        print("seleccione una opcion valida para el tipo de moneda")

    if input("desea salir de la aplicacion (Y/N)").upper() == "Y":
        break