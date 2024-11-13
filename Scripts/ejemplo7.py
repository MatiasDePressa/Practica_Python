import tkinter as tk

def Destruir():
    ventana.destroy()
    
def Crear():
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Nueva Ventana")
    nueva_ventana.geometry(f'200x200')
    tk.Label(nueva_ventana, text="Nueva ventana").pack()

ventana = tk.Tk()
ventana.title("ejemplo 3")
ventana.geometry(f'500x500')

boton1 = tk.Button(ventana, text="Destruir", command=Destruir).pack()

boton2 = tk.Button(ventana, text="Crear", command=Crear).pack()

ventana.mainloop()