import tkinter as tk
from tkinter import messagebox #inportamos el modulo messagebox

def mostrar_saludo(): #vamos a crear la funcion
    nombre = entrada_nombre.get() #get() obtione el dato dentro de una variable
    saludo = f'Hola {nombre}' #va a crear una variable con el saludo
    messagebox.showinfo("Saludo a un nombre", saludo) # va a mostrar el saludo

ventana = tk.Tk() #creamos la ventana
ventana.title("Saludo con boton") #vamos a darle un titulo a la ventana 

texto = tk.Label(ventana, text="Ingrese su nombre") #vamos a colocar un mensaje
texto.pack() #vamos a acomodar el texto dentro de la ventana
entrada_nombre= tk.Entry(ventana, font=("Helvetica", 24))
#vamos a colocar un input
entrada_nombre.pack() #vamos a colocar el input dentro de la ventana

tk.Button(ventana, text="Mostrar saludo", command=mostrar_saludo).pack() 
#vamos a crear el boton y acomodarlo dentro de la ventana

ventana.mainloop() #ejecutamos el bucle