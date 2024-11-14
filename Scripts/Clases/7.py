class Tiempo:
    def __init__(self, horas=0, minutos=0, segundos=0):
        if horas < 0 or minutos < 0 or segundos < 0:
            raise Exception("El tiempo no puede ser puede ser negativo, no es volver al futuro")
        else:
            self.horas = horas
            self.minutos = minutos
            self.segundos = segundos

    def __str__(self):
        return f'({self.horas:.2f} : {self.minutos:.2f} : {self.segundos})'
    

    def tiempoEnHoras(self):
        return self.horas + self.minutos / 60 + self.segundos / 3600

    def tiempoEnMinutos(self):
        return self.horas * 60 + self.minutos + self.segundos / 60

    def tiempoEnSegundos(self):
        return self.horas * 3600 + self.minutos * 60 + self.segundos
    
    def duracionDeTiempo(tiempo1, tiempo2):
        return tiempo1 if tiempo1.tiempoEnHoras()>=tiempo2.tiempoEnHoras() else tiempo2

    

tiempo1 = Tiempo(60,120,3600)
tiempo2 = Tiempo(40,120,3600)
print(tiempo1, tiempo2)
print(tiempo1.tiempoEnHoras())
print(Tiempo.duracionDeTiempo(tiempo1, tiempo2))
