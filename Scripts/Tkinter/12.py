import tkinter as tk
from tkinter import PhotoImage

def salir_pantalla_completa(event):

    ventana.attributes('-fullscreen', False)

def pantalla_completa(event):

    ventana.attributes('-fullscreen', True)

def Destruir():
    ventana.destroy()

ventana = tk.Tk()
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ventana.geometry(f"{ancho_pantalla//2}x{alto_pantalla//2}")
ventana.attributes('-fullscreen', True)

tk.Button(ventana, text="salir", command=Destruir).pack()

ventana.bind("<F11>", pantalla_completa)
ventana.bind("<Escape>", salir_pantalla_completa)

imagen_fondo = PhotoImage(file="imagen.png")
fondo_label = tk.Label(ventana, image=imagen_fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

boton=tk.Button(ventana, text="salir", command=Destruir)
boton.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
ventana.mainloop()


