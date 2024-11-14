import tkinter as tk

ventana = tk.Tk()

ancho = 500 #se declara la variable del ancho
alto = 500 #se declara la variable del alto

ancho_pantalla = ventana.winfo_screenwidth() #obtiene las dimensiones del ancho
alto_pantalla = ventana.winfo_screenheight() #obtiene las dimensiones del alto

pos_x = (ancho_pantalla - ancho) #declaramos las variables de calculo para el ancho
pos_y = (alto_pantalla - alto) #declaramos las variables de calculo para el alto


#ventana.geometry(f'500x500+900+900')
ventana.geometry(f'{ancho}x{alto}+{pos_x//2}+{pos_y//2}')
#determina el tamaño y la posicion
#el formato siempre es el mismo, los primeros dos numeros son el tamaño
#y los ultimos dos la posicion

ventana.mainloop()