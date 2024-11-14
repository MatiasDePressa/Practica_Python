import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de Propiedades")

# Cuadro de entrada con texto y fuente personalizada
entrada = tk.Entry(ventana, text="Texto aquí", font=("Arial", 12))
entrada.pack(pady=20)

ventana.mainloop()
