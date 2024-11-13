import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de Propiedades")

# Cuadro de entrada para contraseña con caracteres ocultos
entrada_contraseña = tk.Entry(ventana, show="*")
entrada_contraseña.pack(pady=20)

# Cuadro de entrada deshabilitado
entrada_deshabilitada = tk.Entry(ventana, state="disabled")
entrada_deshabilitada.pack(pady=20)

ventana.mainloop()