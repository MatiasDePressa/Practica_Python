class Publicacion:
    def __init__(self, titulo, autor="indefinido"):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} por {self.autor}"
    
    def Lectura(self):
        raise NotImplementedError("Aca no")

class Libro(Publicacion):
    def __init__(self, titulo, autor, num_paginas):
        super().__init__(titulo, autor)
        self.num_paginas = num_paginas

    def __str__(self):
        return f"Libro: {super().__str__()} ({self.num_paginas} páginas)"
    
    def Lectura(self):
        return f'Leyendo...'

class Revista(Publicacion):
    def __init__(self, titulo, autor, numero_edicion):
        super().__init__(titulo, autor)
        self.numero_edicion = numero_edicion

    def __str__(self):
        return f"Revista: {super().__str__()} - Edición {self.numero_edicion}"

    def Lectura(self):
        return f'Leyendo...'
    
class Capitulo(Libro):
    def __init__(self, titulo, autor, num_paginas, numero_capitulo, titulo_capitulo, num_paginas_capitulo):
        super().__init__(titulo, autor, num_paginas)
        self.numero_capitulo = numero_capitulo
        self.titulo_capitulo = titulo_capitulo
        self.num_paginas_capitulo = num_paginas_capitulo

    def __str__(self):
        return f'Capitulo {self.numero_capitulo}: {self.titulo_capitulo} ({self.num_paginas_capitulo} paginas) del {super().__str__()}'


# Crear objetos
libro1 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", 1178)
revista1 = Revista("National Geographic", "Variado", 2024)
capitulo1 = Capitulo("El Señor de los Anillos", "J.R.R. Tolkien", 1178, 1, "una comunidad se forma", 30)

# Usar el método __str__ para imprimir detalles
print(libro1.Lectura())  # Libro: El Señor de los Anillos por J.R.R. Tolkien (1178 páginas)
print(revista1)  # Revista: National Geographic por Variado - Edición 2024
print(capitulo1)
