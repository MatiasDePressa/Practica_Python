import tkinter as tk
from tkinter import messagebox #importamos el modulo messagebox

def Saludo(): #creamos la funcion saludo
    nombre = entrada.get() #Obtenemos el dato de la variable y lo inicializamos en otra
    saludo = f'hola {nombre}' #creamos un saludo
    messagebox.showinfo("Saludo", saludo) #creamos la cajita de texto y mostramos el saludo

ventana = tk.Tk()
ventana.title("mensaje")
ventana.geometry(f'500x500')

text = tk.Label(ventana, text="Ingrese un nombre:")
text.pack()

entrada = tk.Entry(ventana) #creamos un widget imput
entrada.pack()

tk.Button(ventana, text="mostrar saludo", command=Saludo).pack() #creamos un boton que ejecuta la funcion

ventana.mainloop()