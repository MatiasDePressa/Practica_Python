import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("centrar ventana")

def centrar_ventana(ventana, width, heigth):
    screen_width = ventana.winfo_screenwidth()
    screen_heigth = ventana.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_heigth - heigth) //2

    ventana.geometry(f'{width}x{heigth}+{x}+{y}')


alto_ventana = 200
ancho_ventana = 400

centrar_ventana(root, ancho_ventana, alto_ventana)

label = tk.Label(root, text="hola mundo", font=("Arial",20)).pack(pady=15)

def Saludo():
    nombre = entrada.get()
    saludo = f'hola {nombre}'
    messagebox.showerror("Saludo", saludo)
    messagebox.showinfo("Saludo", saludo)
    messagebox.showwarning("Saludo", saludo)

text= tk.Label(root, text="ingrese un nombre").pack()

entrada = tk.Entry(root)
entrada.pack()

boton = tk.Button(root, text="mostrar saludo", command=Saludo).pack()

def Destruir():
    root.destroy()

def Crear():
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("nueva ventana")
    nueva_ventana.geometry(f'100x100')
    tk.Label(nueva_ventana, text="nueva ventana!!!!").pack()

boton_destruir = tk.Button(root, text="Destrucion", command=Destruir)
boton_destruir.pack()

boton_crear = tk.Button(root, text="crear ventana", command=Crear)
boton_crear.pack()

root.mainloop()