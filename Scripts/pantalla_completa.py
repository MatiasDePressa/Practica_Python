import tkinter as tk

def pantalla_completa(event):
    ventana.attributes('-fullscreen', True)

def salir_pantalla_completa(event):
    ventana.attributes('-fullscreen', False)

ventana = tk.Tk()
ventana.title("panatalla completa")
ventana.geometry(f'720x720')

ventana.bind("<F11>", pantalla_completa)
ventana.bind("<Escape>", salir_pantalla_completa)

ventana.mainloop()