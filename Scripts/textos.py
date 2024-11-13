import tkinter as tk
from tkinter import PhotoImage

ventana = tk.Tk()
ventana.title("ejemplo de textos")
ventana.geometry(f'500x500')

imagen_fondo = tk.PhotoImage(file="clase 4\imagen.png")
etiqueta_fondo=tk.Label(ventana, image=imagen_fondo)
etiqueta_fondo.place(x=0, y=0, relwidth=1, relheight=1)

texto = tk.Label(ventana, text="Hola mundo", font=("Verdana",24,"bold"), fg="blue", bg="green", height=3, width=15)
texto.grid(row=0, column=0, padx=((500-15)/5), pady=((500-3)/3))

ventana.mainloop()