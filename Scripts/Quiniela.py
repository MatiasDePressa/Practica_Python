import random

class Quiniela:
    def __init__ (self, primer_numero=0, segundo_numero=0, apuesta=0):
        if primer_numero < 0 or segundo_numero < 0 or apuesta <= 1:
            raise Exception("Los valores no pueden ser negativos")
        elif primer_numero == segundo_numero:
            raise Exception("No se puede seleccionar dos veces el mismo número.")
        self.primer_numero = primer_numero
        self.segundo_numero = segundo_numero
        self.apuesta = apuesta
        self.numero_ganador = random.randint(0,99)

    def __str__ (self):
        return f'Primer Numero Seleccionado: {self.primer_numero}\nSegundo Numero Seleccionado: {self.segundo_numero}\nApuesta Total: {self.apuesta}'
    
    
    def ganadorQuiniela(self):
        if self.primer_numero == self.numero_ganador:
            premio = "Primer Premio"
        elif self.segundo_numero == self.numero_ganador:
            premio = "Segundo Premio"
        else:
            premio = "No hubo ganancia"
        return premio
    
    def gananciaDeApuesta(self):
        if self.primer_numero == self.numero_ganador:
            return self.apuesta * 50
        elif self.segundo_numero== self.numero_ganador:
            return self.apuesta * 25
        return "No hubo ganacia"

quiniela_1 = Quiniela(3,6,100)
print(quiniela_1.numero_ganador)
print(quiniela_1.gananciaDeApuesta())