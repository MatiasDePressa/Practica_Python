import tkinter as tk #importamos la libreria
root = tk.Tk() #creamos la ventana
root.title("mi primera ventana") #le damos un titulo a la ventana
root.geometry("800x800") #le damos un tamaño a la ventana

canvas = tk.Canvas(root, width=800, height=400, bg="gray")
canvas.pack()

canvas.create_rectangle(50, 50, 150, 150, fill="blue")

canvas.create_oval(200, 100, 300, 150, fill="red")

canvas.create_line(50, 200, 300, 200, fill="green", width=3)

listbox = tk.Listbox(root, height=10, selectmode=tk.SINGLE)
listbox.pack()

item = ["opcion1", "opcion2", "opcion3", "opcion4"]
for opciones in item:
    listbox.insert(tk.END, opciones)

text = tk.Text(root, wrap=tk.WORD, width=40, height=10)
scrollbar = tk.Scrollbar(root, command=text.yview)
text.config(yscrollcommand=scrollbar.set)

text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

for i in range(0,101):
    text.insert(tk.END, f'linea {i} \n')

root.mainloop() #ejecutamos la ventana