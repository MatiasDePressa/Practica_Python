import tkinter as tk

def la_destruccion():
    nueva_ventana = tk.Toplevel(ventana)
    #coloca la nueva ventana arriba de la anterior
    nueva_ventana.title("LA DESTRUCCION")
    tk.Label(nueva_ventana, text="BIENVENIDO A LA DESTRUCCION").pack()
    #mostrar un texto en la nueva ventana y empaquetarlo

def la_salvacion():
    ventana.destroy() #selecciona un elemento y lo elimina

ventana = tk.Tk() #vamos a crear la ventana
ventana.title("Elige: Salvacion o Destruccion") #le vamos a dar un titulo
ventana.geometry(f'500x500+400+400')

boton1=tk.Button(ventana, text="La Destruccion", command=la_destruccion)
#creamos el boton que crea la nueva ventana
boton = tk.Button(ventana, text="La Salvacion", command=la_salvacion)
boton.grid(row=1,column=2)
boton1.grid(row=1,column=1)
#crea el boton que elimina la ventana

ventana.mainloop()