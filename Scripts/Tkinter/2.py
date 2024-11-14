import tkinter as tk

def Crear_ventana():
    nueva_ventana=tk.Toplevel(ventana)#crea la nueva ventana
    nueva_ventana.title("Nueva ventana")#le da un titulo a la nueva ventana
    tk.Label(nueva_ventana, text="Nueva ventana").pack()#coloca el texto y lo muestra

def Destruccion():
    ventana.destroy()#destruye todas las ventanas

ventana = tk.Tk() 
ventana.title("botones")
ventana.geometry(f'300x300+1000+600') #aqui le damos el tamaño y la posicion a la ventana

boton1=tk.Button(ventana, text="Destruir", command=Destruccion).pack()
boton2=tk.Button(ventana, text="crear nueva ventana", command=Crear_ventana).pack()



ventana.mainloop()