class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Usamos _ para indicar que es "privado"
        self._edad = edad

    # Getter para nombre
    def get_nombre(self):
        return self._nombre

    # Setter para nombre
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    # Getter para edad
    def get_edad(self):
        return self._edad

    # Setter para edad
    def set_edad(self, nueva_edad):
        if nueva_edad > 0:  # Validación sencilla
            self._edad = nueva_edad
        else:
            print("La edad debe ser positiva.")

# Crear una instancia de la clase Persona
persona1 = Persona("Matías", 30)

# Usar los getters para obtener los atributos
print(persona1.get_nombre())  # Matías
print(persona1.get_edad())    # 30

# Cambiar los atributos usando los setters
persona1.set_nombre("Carlos")
persona1.set_edad(35)

# Obtener los atributos modificados
print(persona1.get_nombre())  # Carlos
print(persona1.get_edad())    # 35
