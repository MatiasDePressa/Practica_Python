import numpy as np

def validarTipo(variable, nombre, tipo):
  if isinstance(variable, tipo):
    return variable
  else:
    raise Exception("La variable " + nombre + " debe ser de tipo " + str(tipo) + ".")


# asumiremos que la hora es un entero
class Auto:
  def __init__(self, patente, horaIngreso):
    self._patente = validarTipo(patente,"patente",str)
    self._horaIngreso = validarTipo(horaIngreso,"horaIngreso",int)
    self._horaEgreso = None

  def __repr__(self):
    return str(self._patente)+" "+str(self._horaIngreso)+" "+str(self._horaEgreso)

class Sector:
  def __init__(self, capacidad, valorHora):
    self._capacidad = capacidad     
    self._valorHora = valorHora 
    self._autos = np.zeros(self._capacidad,Auto) 

  def __repr__(self):
    ret = ""
    for i in range(len(self._autos)):
      if self._autos[i] != 0:
        ret += str(self._autos[i]) + ","
    return ret

  def ingresarAuto(self, auto):
  #lo asigno en el 1er lugar libre o doy un error
    primerLugarLibre = 0
    while self._autos[primerLugarLibre] != 0 and primerLugarLibre < self._capacidad:
      primerLugarLibre +=1

    if primerLugarLibre == self._capacidad:
      raise Exception("No hay lugar")
    else:
      self._autos[primerLugarLibre] = auto
    
  def egresarAuto(self, patente, horaSalida):
    for i in range(len(self._autos)):
      if self._autos[i] != 0:
        if self._autos[i]._patente == patente:
          self._autos[i]._horaEgreso = horaSalida
          # o bien
          # self._autos[i] = 0

  def calcularPlata(self):
    plata = 0
    for i in range(len(self._autos)):
      if self._autos[i] != 0:  
        if self._autos[i]._horaEgreso != None:
          plata += (self._autos[i]._horaEgreso - self._autos[i]._horaIngreso)*self._valorHora
    return plata


class Estacionamiento:
  def __init__(self):
    # si hacen tres arreglos en lugar de "sectores", tienen que tener el menos el valor hora de cada uno aca...
    self._sectorDocente = Sector(50,10) # capacidad, valor hora
    self._sectorAlumno = Sector(50,5)  
    self._sectorGeneral = Sector(100,20)     

  def __repr__(self):
    ret = "Sector Docente " + str(self._sectorDocente)
    ret += "Sector Alumno " + str(self._sectorAlumno)
    ret += "Sector General " + str(self._sectorGeneral)
    return ret

  def ingresarAuto(self, sector, patente, horaIngreso): 
    patente = validarTipo(patente,"patente",str) 
    sector = validarTipo(sector,"sector",str) 
    if sector == "Docente":
      self._sectorDocente.ingresarAuto(Auto(patente, horaIngreso))
    if sector == "Alumno":
      self._sectorAlumno.ingresarAuto(Auto(patente, horaIngreso))
    if sector == "General":
      self._sectorGeneral.ingresarAuto(Auto(patente, horaIngreso))
    

# aca pueden decidir entre borrar el auto o ponerle hora de salida
# si le ponene hora de salida, solo se deben sumar esos autos
# para calcular el dinero recaudado
  def egresarAuto(self, sector, patente, horaSalida):
    patente = validarTipo(patente,"patente",str) 
    sector = validarTipo(sector,"sector",str) 
    if sector == "Docente":
      self._sectorDocente.egresarAuto(patente, horaSalida)
    if sector == "Alumno":
      self._sectorAlumno.egresarAuto(patente, horaSalida)
    if sector == "General":
      self._sectorGeneral.egresarAuto(patente, horaSalida)

  def calcularPlata(self):
    ret = 0
    ret += self._sectorDocente.calcularPlata()
    ret += self._sectorAlumno.calcularPlata()
    ret += self._sectorGeneral.calcularPlata()
    return ret

# codigo cliente minimo que tiene que correr para aprobar
# opcional: validar tipos. validar horasalida > horaentrada
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