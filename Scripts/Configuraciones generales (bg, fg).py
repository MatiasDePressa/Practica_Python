import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de Propiedades")

# Etiqueta con color de fondo y color de texto
etiqueta = tk.Label(ventana, text="Hola, Mundo!", bg="lightblue", fg="navy")
etiqueta.pack(padx=10, pady=10)

ventana.mainloop()
