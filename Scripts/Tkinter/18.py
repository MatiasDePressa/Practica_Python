import tkinter as tk #importamos la libreria
from tkinter import colorchooser
root = tk.Tk() #creamos la ventana
root.title("mi primera ventana") #le damos un titulo a la ventana
root.geometry("800x800") #le damos un tamaño a la ventana

spinbox = tk.Spinbox(root, from_=0, to=20, increment=1, width=10)
spinbox.pack(padx=10, pady=10)

scale_vertical = tk.Scale(root, from_=0, to=100, orient=tk.VERTICAL)
scale_vertical.pack()

scale_horizontal = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
scale_horizontal.pack()

def Hola():
    print("Hola")

menu1 = tk.Menu(root)

menu2 = tk.Menu(menu1, tearoff=0)
menu2.add_command(label="opcion1", command=Hola)
menu2.add_command(label="opcion2", command=Hola)
menu2.add_command(label="opcion3", command=Hola)
menu2.add_command(label="opcion4", command=Hola)
menu2.add_command(label="opcion5", command=Hola)
menu2.add_command(label="opcion6", command=Hola)
menu2.add_separator()
menu2.add_command(label="opcion7", command=root.quit)

menu1.add_cascade(label="opcion 8", menu=menu2)

root.config(menu=menu1, bg="gray")

def Actualizar():
    entry = entrada.get()
    label.config(text=entry)

def Cambiar_Color():
    color = colorchooser.askcolor(title="Selecciona un color")[1]
    if color!=None:
        label.config(bg=color)

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

entrada = tk.Entry(frame, width=40)
entrada.pack()

boton = tk.Button(frame, text="actualizar", command=Actualizar)
boton.pack()

label = tk.Label(frame, text="texto aca", width=40, height=5, bg="red", font=("Arial", 20))
label.pack()

boton2 = tk.Button(frame, text="cambiar color de fondo", command=Cambiar_Color)
boton2.pack()

root.mainloop() #ejecutamos la ventana