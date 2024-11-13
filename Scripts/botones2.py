import tkinter as tk

def toggle_pantalla_completa(event):
    if ventana.attributes('-fullscreen'):
        ventana.attributes('-fullscreen', False)
    else:
        ventana.attributes('-fullscreen', True)

ventana = tk.Tk()
ventana.title("Toggle Pantalla Completa")

# Configurar evento de tecla para pantalla completa y salida de pantalla completa
ventana.bind("<F11>", toggle_pantalla_completa)
ventana.bind("<Escape>", toggle_pantalla_completa)

# Etiqueta informativa
etiqueta = tk.Label(ventana, text="Presiona F11 para pantalla completa y Escape para salir", font=("Arial", 14))
etiqueta.pack(pady=20)

ventana.mainloop()
