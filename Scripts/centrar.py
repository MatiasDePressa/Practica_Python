import tkinter as tk

ventana=tk.Tk()

ancho = 500 #darle un ancho a la ventana
alto = 500 #darle un alto a la ventana

ancho_pantalla = ventana.winfo_screenwidth() #tomo el ancho de la pantalla de la persona
alto_pantalla = ventana.winfo_screenheight() #tomo el alto de la pantalla de la persona

pos_x = (ancho_pantalla - ancho) #voy a utilizar estas varibles para centrar la ventana
pos_y = (alto_pantalla - alto)

ventana.geometry(f'{ancho}x{alto}+{pos_x//2}+{pos_y//2}')
#voy a darle un tamaño y posicion a la ventana en base a la pantalla del usuario

ventana.mainloop()