#creacion de la clase
class Persona:
    #pass palabra reservada para indicar que la clase esta vacia
    def __init__(self, altura, peso, edad, nombre):
        self.altura = altura
        self.peso = peso
        self.edad = edad
        self.nombre = nombre

    def __repr__(self):
        return f'Persona({self.altura},{self.peso},{self.edad},{self.nombre})'
    
    def __str__(self):
        return f'Nombre: {self.nombre}\nAltura: {self.altura}\nPeso:{self.peso}\nEdad: {self.edad}'
    
    def Saludar(self):
        return f'Hola soy {self.nombre}'
    
    def CambiarNombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        return f'mi nuevo nombre es: {self.nombre}'
    
class Estudiante(Persona):#creo una clase hijo con la clase padre como parametro
    def __init__(self, persona:Persona, carrera):
        super().__init__(persona.altura, persona.peso, persona.edad, persona.nombre)
        self.carrera = carrera

    def __str__(self):
        return f'Nombre: {self.nombre}\nAltura: {self.altura}\nPeso:{self.peso}\nEdad: {self.edad}\nCarrera: {self.carrera}'

#instancia
persona1 = Persona(1.70, 65, 20, "ramon")
persona2 = Persona(1.90, 80, 19, "PEPE")
print(persona2)
print(persona2.CambiarNombre("Martin"))
print(persona2)
print()
estudiante1 = Estudiante(persona1, "programacion")
print(estudiante1)
