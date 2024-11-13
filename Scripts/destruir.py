import tkinter as tk

def crear_nueva_ventana():
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Nueva Ventana")
    tk.Label(nueva_ventana, text="¡Nueva Ventana!").pack(padx=20, pady=20)

def cerrar_todas_ventanas():
    root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Control de Ventanas")

# Botón para crear una nueva ventana
tk.Button(root, text="Crear Nueva Ventana", command=crear_nueva_ventana, font=("Helvetica", 14)).pack(pady=20)

# Botón para cerrar todas las ventanas
tk.Button(root, text="Cerrar Todas las Ventanas", command=cerrar_todas_ventanas, font=("Helvetica", 14)).pack(pady=20)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
