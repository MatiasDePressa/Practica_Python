import tkinter as tk

ventana = tk.Tk()

ancho = ventana.winfo_screenwidth()
alto = ventana.winfo_screenheight()

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

pos_x = (ancho_pantalla - ancho)
pos_y = (alto_pantalla - alto)

ventana.geometry(f'{ancho}x{alto}+0+0')

ventana.mainloop()