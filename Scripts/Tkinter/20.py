import tkinter as tk
from tkinter import messagebox #llamamos al modulo messagebox

def mostrar_saludo(): #creamos una funcion para mostrar y crear nuestra ventana secundaria
    nombre = entrada_nombre.get() #tomamos el dato del input
    saludo = f'hola {nombre}' #creamos un saludo
    messagebox.showinfo("hola", saludo) #creamos la ventana y mostramos el saludo

ventana = tk.Tk() #creamos la ventana
ventana.title("saludo con boton") #le damos un titulo a la ventana

texto= tk.Label(ventana, text="ingrese su nombre").pack() #creamos y mostramos un texto
entrada_nombre = tk.Entry(ventana).pack() #creamos y mostramos el input

boton=tk.Button(ventana, text="mostrar saludo", command=mostrar_saludo).pack()
#creamos y mostramos el boton; y ejecutamos la funcion al presionar

ventana.mainloop()#ejecutamos la ventana