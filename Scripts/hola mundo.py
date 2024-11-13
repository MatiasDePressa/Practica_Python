import tkinter as tk
def mostrar_hola_mundo():
    
    ventana = tk.Tk()
    etiqueta = tk.Label(ventana, text="Hola mundo", font=("Helvetica", 16))
    etiqueta.pack(padx=20, pady=20)
    ventana.mainloop()

mostrar_hola_mundo()
