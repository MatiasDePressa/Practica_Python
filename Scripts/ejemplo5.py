#pip install tkinter
#pip3 install tkinter

import tkinter as tk #importamos la libreria

ventana=tk.Tk() #creamos la ventana
etiqueta=tk.Label(ventana, text="Hola mundo") #creamos nuestro texto
etiqueta.pack() #lo colocamos dentro de la ventana

ventana.title("Hola mundo") #le damos un titulo a la ventana
ventana.geometry(f'500x500+400+400') #con esto le damos posiciones y una dimension

boton = tk.Button(ventana, text="haz click", command= lambda: print("click")) #creamos el boton y damos una funcion
boton.pack() #colocamos el boton dentro de la ventana 

ventana.mainloop() #ejecutamos la ventana