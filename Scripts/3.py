class Animal:
    def Correr(self):
        return f'el animal puede correr'
    
class Pez:
    def Nadar(self):
        return f'el pez puede nadar'
    
class Pinguino(Animal, Pez):
    pass

pinguino = Pinguino()

print(pinguino.Correr())
print(pinguino.Nadar())