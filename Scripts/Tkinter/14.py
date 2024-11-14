import tkinter as tk

def click_button(value):
    print(f"Botón {value} presionado")

root = tk.Tk()
root.title("Pad Numérico")

# Crear botones del 1 al 9
for i in range(1, 10):
    button = tk.Button(root, text=str(i), command=lambda val=i: click_button(val), width=5, height=2)
    button.grid(row=(i-1)//3, column=(i-1)%3)

root.mainloop()
