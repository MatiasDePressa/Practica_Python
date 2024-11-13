import tkinter as tk
from tkinter import messagebox

def mostrar_saludo():
    nombre = entrada_nombre.get()
    saludo = f"Hola {nombre}"
    messagebox.showinfo("Saludo", saludo)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Saludo App")

# Etiqueta y entrada para ingresar el nombre
tk.Label(ventana, text="Ingrese su nombre:").pack(pady=10)
entrada_nombre = tk.Entry(ventana, font=("Helvetica", 12))
entrada_nombre.pack(pady=10)

# Botón para mostrar el saludo
tk.Button(ventana, text="Mostrar Saludo", command=mostrar_saludo, font=("Helvetica", 14)).pack(pady=10)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
