import matplotlib.pyplot as plt
import numpy as np

# Definimos la función que queremos graficar
def f(x):
    return x**2 + 2*x + 1

# Generamos un array de x
x = np.linspace(-10, 10, 400)

# Calculamos los valores de y
y = f(x)

# Creamos la gráfica
plt.plot(x, y)

# Agregamos título y etiquetas
plt.title('Gráfica de la función f(x) = x^2 + 2x + 1')
plt.xlabel('x')
plt.ylabel('f(x)')

# Mostramos la gráfica
plt.grid(True)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.show()