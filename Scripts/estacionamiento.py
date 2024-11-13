import numpy as np

class Auto:
    def __init__(self, patente="",horaingreso=0):
        if len(patente)>3 or len(patente)<0:
            raise Exception
        else:
            self.patente=patente
            self.horaingreso=horaingreso
            self.horaEgreso = None

    def __repr__(self):
        return "la pantente es "+str(self.patente)+" y la hora de ingreso es "+str(self.horaingreso)

class Sector:
    def __init__(self, capacidad, valorhora):
      self.capacidad = capacidad     
      self.valorhora = valorhora 
      self.ocupado = np.zeros(self.capacidad)

    def __repr__(self):
        suma = ""
        for i in range(len(self.ocupado)):
            if self.ocupado[i] != 0:
                suma += str(self.ocupado[i]) + ","
            return suma

    def ingresarAuto(self, Auto):
        primerLugarLibre = 0
        while self.ocupado[primerLugarLibre] != 0 and primerLugarLibre < self.capacidad:
            primerLugarLibre +=1

        if primerLugarLibre == self.capacidad:
            raise Exception("No hay lugar")
        else:
            self.ocupado[primerLugarLibre] = Auto
    
    def egresarAuto(self, patente, horaSalida):
        for i in range(len(self.ocupado)):
            if self.ocupado[i] != 0:
                if self.ocupado[i].patente == patente:
                    self.ocupado[i].horaEgreso = horaSalida

class Estacionamiento:
  def __init__(self):
    self.sectorDocente = Sector(50,10)
    self.sectorAlumno = Sector(50,5)  
    self.sectorGeneral = Sector(100,20)     

  def __repr__(self):
    suma = "Sector Docente " + str(self.sectorDocente)
    suma += "Sector Alumno " + str(self.sectorAlumno)
    suma += "Sector General " + str(self.sectorGeneral)
    return suma

  def ingresarAuto(self, sector="", patente="", horaIngreso=0): 
    if sector == "Docente":
      self.sectorDocente.ingresarAuto(Auto(patente, horaIngreso))
    if sector == "Alumno":
      self.sectorAlumno.ingresarAuto(Auto(patente, horaIngreso))
    if sector == "General":
      self.sectorGeneral.ingresarAuto(Auto(patente, horaIngreso))
    

  def egresarAuto(self, sector="", patente="", horaSalida=""):
    if sector == "Docente":
      self.sectorDocente.egresarAuto(patente, horaSalida)
    if sector == "Alumno":
      self.sectorAlumno.egresarAuto(patente, horaSalida)
    if sector == "General":
      self.sectorGeneral.egresarAuto(patente, horaSalida)

  def calcularPlata(self):
    suma = 0
    suma += self.sectorDocente.calcularPlata()
    suma += self.sectorAlumno.calcularPlata()
    suma += self.sectorGeneral.calcularPlata()
    return suma

def calcularPlata(self):
    plata = 0
    for i in range(len(self.ocupado)):
      if self.ocupado[i] != 0:  
        if self.ocupado[i].horaEgreso != None:
          plata += (self.ocupado[i].horaEgreso - self.ocupado[i].horaIngreso)*self.valorhora
    return plata

e = Estacionamiento()
e.ingresarAuto("Docente","aaa",1)
e.ingresarAuto("Docente","bbb",2)
e.ingresarAuto("Alumno","ccc",3)
e.ingresarAuto("General","ddd",3)
e.ingresarAuto("General","eee",3)
e.egresarAuto("Docente","bbb",4)
e.egresarAuto("Alumno","ccc",5)
e.egresarAuto("General","ddd",5)
print(e)
print(e.calcularPlata())