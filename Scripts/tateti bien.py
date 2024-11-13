import numpy as np #importamos Numpy
import tkinter as tk #importamos tkinter
from tkinter import messagebox #llamamos al modulo messagebox

def inicializar_juego():
    global jugador_actual, tablero #creamos las variables globales jugador_actual y tablero
    jugador_actual= "X" #establecemos al jugador actual como "X"
    tablero = np.empty((3,3), dtype=str) #creamos una matriz vacia con datos de tipo str

    for fila_recorrido in range(3): #recorremos las filas
        for columna_recorrido in range(3): #recorremos las columnas
            boton = tk.Button(ventana, text="", width=5, height=2, command=lambda fila=fila_recorrido, columna= columna_recorrido: al_click(fila, columna))
            #creamos un boton que contenga un texto vacio, que va a tener un alto y un ancho, y al presionarlo se ejecuta un comando
            #que inicializa las variables fila y columna, las envia a la funcion al_click y ejecuta esta misma funcion
            boton.grid(row=fila_recorrido, column=columna_recorrido) 
            #genera una matriz dentro de la ventana y ordena los botenes dentro de la ventana en base a la matriz del tablero

def al_click(fila, columna):
    global jugador_actual #toma al jugador actual
    if tablero[fila, columna]=="": #verifica si el lugar en el que queremos colocar nuestro dato esta vacio
        tablero[fila, columna]=jugador_actual #en caso de que este vacio colocara al juagador actual
        actualizar_boton(fila, columna) #actualiza el boton
        if hay_ganador(): #verifica si hay un ganador
            messagebox.showinfo("felicidades",f'Felicidades, el jugador {jugador_actual} ha ganado')
            #si hay ganador generara una ventana de informacion con un mensaje de felicitaciones
            reiniciar_juego() #reinicia el juego
        elif "" not in tablero: #en caso de que ya no haya espacios vacios dentro de la matriz, entonces:
            messagebox.showinfo("empate", "han empatado") #muestra un mensaje de empate
            reiniciar_juego() #reinicia el juego
        else:
            cambiar_jugador() #en caso de que no haya ganador ni empate cambia de jugador
        
def actualizar_boton(fila, columna):
    boton = ventana.grid_slaves(row=fila, column=columna)[0] #crea un array con la longitud y los datos
    #de la matriz de la ventana (el grid de la ventana) o en caso de que ya exista esta matriz agrega los datos 
    boton.config(text=jugador_actual, state=tk.DISABLED) #configura el boton para mostrar al jugador actual y 
    #para que no se pueda volver a presionar el boton

def cambiar_jugador():
    global jugador_actual #llama al jugador actual
    if jugador_actual=="X": #en caso de que el actual sea "X" lo cambia por "O"
        jugador_actual="O"
    else: #y en caso de que sea "O" lo cambia por "X"
        jugador_actual="X"

def hay_ganador():
    for i in range(3):
        if tablero[i, 0] == tablero[i, 1] == tablero[i, 2] == jugador_actual:
            return True
            #recorre las filas del tablero y si son las tres iguales retorna True
        elif tablero[0, i] == tablero[1, i] == tablero[2, i] == jugador_actual:
            return True
            #recorre las columnas del tablero y si son todas iguales retorna True
    if tablero[0, 0] == tablero[1, 1] == tablero[2, 2] == jugador_actual:
        return True
        #recorre la diagonal principal
    elif tablero[0, 2] == tablero[1, 1] == tablero[2, 0] == jugador_actual:
        return True
        #recorre la diagonal secundaria
    return False
    #en caso de que ninguna de las condiciones se cumpla retorna False

        
def reiniciar_juego():
    global jugador_actual, tablero
    jugador_actual="X" #sobreescribe todos los datos como al inicio
    tablero = np.empty((3,3), dtype=str)

    for boton in ventana.grid_slaves(): #utiliza la matriz del tablero para reiniciar los botones
        boton.config(text="", state=tk.NORMAL)

ventana= tk.Tk() #Crea la ventana
ventana.title("ta-te-ti") #titulo de la ventana
inicializar_juego() #inicia el juego
ventana.mainloop() #inicia el bucle