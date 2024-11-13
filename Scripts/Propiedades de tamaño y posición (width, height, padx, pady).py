import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de Propiedades")

# Botón con ancho, alto y márgenes específicos
boton = tk.Button(ventana, text="Presiona", width=15, height=2, padx=10, pady=5)
boton.pack(pady=20)

ventana.mainloop()
