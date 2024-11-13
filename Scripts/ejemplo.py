#esto se tiene que colocar en consola para instalar la libreria
#pip install tkinter
#pip3 install tkinter

import tkinter as tk

ventana=tk.Tk() #crea la ventana. Tk: es una clase que contine las funciones
etiqueta=tk.Label(ventana, text="hola mundo") 
etiqueta.pack() #la acomodamos dentro de la ventana

boton = tk.Button(ventana, text="haz click", command=lambda: print("click"))
#se crea un boton, y se utiliza el comando "lambda" que va a ejecutar una accion
boton.pack()

ventana.mainloop()