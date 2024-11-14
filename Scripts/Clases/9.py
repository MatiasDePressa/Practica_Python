import numpy as np

def validarPalo(palo):
  if type(palo) != str:
    raise Exception("El tipo de dato ingresado no es correcto")
  palo = palo.lower()
  palos = np.array(["basto","copa","espada","oro"])
  for i in range(len(palos)):
    if palos[i] == palo:
      return palo

  raise Exception("El palo ingresado no existe")

def validarNumero(numero):
  if type(numero) != int:
    raise Exception("El tipo de dato ingresado no es correcto")
  numeros = np.array([1,2,3,4,5,6,7,10,11,12])
  for i in range(len(numeros)):
    if numeros[i] == numero:
      return numero
  raise Exception("El numero ingresado no coincide con las cartas españolas")


class Carta:
  def init(self, numero, palo):
    self.numero = validarNumero(numero)
    self.palo = validarPalo(palo)

  def repr(self):
    return f'La carta es el {self.numero} de {self.palo}'

class Truco:
  def init(self, cartaUno, cartaDos, cartaTres):
    self.cartaUno = Carta(cartaUno.numero, cartaUno.palo)
    self.cartaDos = Carta(cartaDos.numero, cartaDos.palo)
    self.cartaTres = Carta(cartaTres.numero, cartaTres.palo)

  def tengoFlor(self):
    # Las 3 cartas deben ser del mismo palo
    if self.cartaUno.palo == self.cartaDos.palo and self.cartaUno.palo == self.cartaTres.palo:
       return f'FLORRRR'
    return f'Mal cantado pibe'
def dosDelMismoPalo(self):

   if self.cartaUno.palo == self.cartaDos.palo and self.cartaUno.palo != self.cartaTres.palo:
     return True
   elif self.cartaUno.palo == self.cartaTres.palo and self.cartaUno.palo != self.cartaDos.palo:
     return True
   elif self.cartaDos.palo == self.cartaTres.palo and self.cartaDos.palo != self.cartaUno.palo:
     return True
   else:
     return False


def esCartaNegra(self,numero):
    if numero == 10 or numero == 11 or numero == 12:
        return True
    return False


def contarTanto(self):
      tanto = 0
      if self.dosDelMismoPalo():
          tanto = 20
      else:
          if self.cartaUno.numero > self.cartaDos.numero and self.cartaUno.numero > self.cartaTres.numero and not self.esCartaNegra(self.cartaUno.numero):
            tanto = self.cartaUno.numero
          elif self.cartaUno.numero < self.cartaDos.numero and self.cartaUno.numero > self.cartaTres.numero and not self.esCartaNegra(self.cartaDos.numero):
            tanto = self.cartaDos.numero
          elif self.cartaUno.numero > self.cartaDos.numero and self.cartaUno.numero < self.cartaTres.numero and not self.esCartaNegra(self.cartaTres.numero):
            tanto = self.cartaTres.numero
          else:
            tanto = 0

      if self.esCartaNegra(self.cartaUno.numero):
              tanto += 0
      else:
              tanto += self.cartaUno.numero

      if self.esCartaNegra(self.cartaDos.numero):
              tanto += 0
      else:
              tanto += self.cartaDos.numero

      if self.esCartaNegra(self.cartaTres.numero):
              tanto += 0
      else:
              tanto += self.cartaTres.numero

      return f'Su tanto es de {tanto}'





mano = Truco(Carta(10,"oro"), Carta(5,"espada"), Carta(3, "copa"))

mano.contarTanto()