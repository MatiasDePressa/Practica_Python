import tkinter as tk

ventana = tk.Tk()
etiqueta = tk.Label(ventana, text="Hola, Tkinter!")
etiqueta.pack()

boton = tk.Button(ventana, text="Haz clic", command=lambda: print("¡Clic!"))
boton.pack()

ventana.mainloop()
