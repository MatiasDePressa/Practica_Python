import math

rangeY = 40  # Máximas y mínimas coordenadas Y que se renderizarán centradas en 0
rangeX = 40  # Máximas y mínimas coordenadas X que se renderizarán centradas en 0
markPoints = 1  # Cuándo mostrar puntos en espacios claros como guía

if rangeY < 1 or rangeX < 1 or markPoints < 1:
    raise Exception("¡Configuración inválida!")

# Pedir la función al usuario
funcion = input("Ingrese la función a graficar (en términos de x): ")

# Reemplazar ^ con ** para que el usuario pueda ingresar potencias con ^
funcion = funcion.replace("^", "**")

for yi in range(rangeY, (-rangeY)-1, -1):
    line = ""
    for xi in range(-rangeX*2, rangeX*2):
        x = xi / 2
        try:
            # Evaluar la función
            y = eval(funcion)
            if yi == math.floor(y):
                line += "X"
            else:
                if yi == 0 or xi == 0:
                    line += "+"
                elif yi % markPoints == 0 and xi % (markPoints * 2) == 0:
                    line += "*" if markPoints > 3 else "."
                else:
                    line += " "
        except Exception as e:
            print(f"Error al evaluar la función: {e}")
            exit()
    print(line)