import tkinter as tk
root = tk.Tk()
root.title("widgets")
root.geometry("800x800")
root.config(bg="lightblue")

root.rowconfigure([0,1,2,3,4,5,6], weight=1)
root.columnconfigure([0,1,2,3,4,5,6], weight=1)

label = tk.Label(root, text="hola mundo", font=("Arial",15), fg="blue", bg="red")
label.grid(row=0, column=3,)

text = tk.Text(root, font=("Georgia",10), height=2)
text.grid(row=1, column=3,)

entry = tk.Entry(root, font="Arial 40", fg="brown", bg="green")
entry.grid(row=2, column=3)

button = tk.Button(root, text="pulsame", command=lambda: label.config(text="adios mundo")).grid(row=3, column=3)

check = tk.IntVar()
checkbox = tk.Checkbutton(root, text="aceptar terminos y condiciones", variable=check, font=("Arial",15)).grid(row=4,column=3)

option = tk.IntVar()
radio1 = tk.Radiobutton(root, text="opcion 1", variable=option, value=1, font=("Arial",15))
radio2 = tk.Radiobutton(root, text="opcion 2", variable=option, value=2, font=("Arial",15))

radio1.grid(row=5,column=3)
radio2.grid(row=5,column=4)

option1 = tk.IntVar()

radio3 = tk.Radiobutton(root, text="opcion 1", variable=option1, value=1, font=("Arial",15))
radio4 = tk.Radiobutton(root, text="opcion 2", variable=option1, value=2, font=("Arial",15))

radio3.grid(row=6,column=3)
radio4.grid(row=6,column=4)

root.mainloop()