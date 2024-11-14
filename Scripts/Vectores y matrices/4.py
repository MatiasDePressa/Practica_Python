import numpy as np

# Inicializar los arrays para almacenar los datos
nombres = np.array([])
cantidades = np.array([])
precios = np.array([])

# Función para agregar un producto al inventario
def agregar_producto(nombre, cantidad, precio):
    global nombres, cantidades, precios  # Indicamos que son variables globales
    if nombre in nombres:
        print("Error: El producto ya existe en el inventario.")
        return
    nombres = np.append(nombres, nombre)
    cantidades = np.append(cantidades, cantidad)
    precios = np.append(precios, precio)
    return nombres, cantidades, precios

# Función para eliminar un producto del inventario
def eliminar_producto(nombre):
    global nombres, cantidades, precios  # Indicamos que son variables globales
    indice = np.where(nombres == nombre)[0]
    if len(indice) == 0:
        print("Error: El producto no existe en el inventario.")
        return
    nombres = np.delete(nombres, indice)
    cantidades = np.delete(cantidades, indice)
    precios = np.delete(precios, indice)
    return nombres, cantidades, precios

# Función para modificar la cantidad de un producto en el inventario
def modificar_cantidad(nombre, nueva_cantidad):
    global nombres, cantidades, precios  # Indicamos que son variables globales
    indice = np.where(nombres == nombre)[0]
    if len(indice) == 0:
        print("Error: El producto no existe en el inventario.")
        return
    if nueva_cantidad < 0:
        print("Error: La cantidad no puede ser negativa.")
        return
    cantidades[indice] = nueva_cantidad
    return cantidades

# Función para calcular el valor total del inventario
def calcular_valor_total():
    global nombres, cantidades, precios  # Indicamos que son variables globales
    return np.sum(cantidades * precios)

def mostrarInventario():
    global nombres, cantidades, precios
    return nombres, cantidades, precios

# Menú para interactuar con el sistema
while True:
    print("Menú:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Modificar cantidad")
    print("4. Calcular valor total")
    print("5. Salir")
    print("6. mostrar")
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio unitario: "))
        agregar_producto(nombre, cantidad, precio)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto: ")
        eliminar_producto(nombre)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del producto: ")
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        modificar_cantidad(nombre, nueva_cantidad)
    elif opcion == "4":
        print("Valor total del inventario: ", calcular_valor_total())
    elif opcion == "5":
        break
    elif opcion=="6":
        print(mostrarInventario())
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")