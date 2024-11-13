class Propiedad:
    """
    clase propiedad:

        parametros:
            - calle : str
            - numero : int
            - localidad : str
            - anio_construccion : int
            - cantidad_ambientes : int

        funcion: 
            almacenar datos de inmuebles y analizarlos, si la propiedad es anterior a 1870, detiene la ejecucion

        operaciones:
            - mayorNumeracion:
                - toma dos propiedades y verifica cual tiene la mayor numeracion si estan en la misma calle, si no estan en la misma calle, detiene la ejecucion
            
            - impuestoARBA:
                - toma una propiedad, verifica el año de construccion y la cantidad de ambientes de esta, y devuelve un porcentaje de impuestos de la misma
    """

    def __init__(self, calle="", numero=0, localidad="", anio_construccion=0, cantidad_ambientes=0):
        #toma por parametros la calle, el numero, la localidad, año de construccion, y la cantidad de ambientes
        #para evitar errores les da un predefinido
        if anio_construccion<1870 or cantidad_ambientes<=0:
            #verifica que el año de construccion sea anterior a 1870, y que la 
            #cantidad de ambientes sea negativa o igual a 0
            #en este caso detendra la ejecucion
            raise Exception("ingresar una propiedad valida")
        #se le dan los valores al objeto teniendo en cuenta los parametros
        self.calle=calle
        self.numero=numero
        self.localidad=localidad
        self.anio_construccion=anio_construccion
        self.cantidad_ambientes=cantidad_ambientes

    def __str__(self):
        # devuelve una cadena de texto con todos los datos del objeto
        return f'calle: {self.calle}, numero: {self.numero}, localidad: {self.localidad}, año de construccion: {self.anio_construccion}, cantidad de ambientes: {self.cantidad_ambientes}'
    
    def mayorNumeracion(propiedad_1, propiedad_2):
        #creo una funcion que toma por parametros dos propiedades
        if propiedad_1.calle == propiedad_2.calle:
        #verifico si ambas propiedades estan en la misma calle
            return propiedad_1.numero if propiedad_1.numero>=propiedad_2.numero else propiedad_2.numero
            #retorno el numero de la propiedad que sea mas alto
        else:
            #en caso de que las propiedades no pertenzcan a la misma calle, detengo la ejecucion
            raise Exception("Las Propiedades deben de estar en la misma calle")
        
    def impuestoARBA(propiedad):
        #creo una funcion que tome por parametros una propiedad
        if propiedad.anio_construccion<=1949:
            #verifico que sea anterior a 1949 
            if propiedad.cantidad_ambientes<3:
                #verifico la cantidad de ambientes y devuelvo un posible resultado
                impuesto = f'5% de impuesto'
            elif propiedad.cantidad_ambientes<6:
                impuesto = f'10% de impuesto'
            else:
                impuesto = f'15% de impuesto'
        else:
            #si la propiedad es posterior a 1949
            if propiedad.cantidad_ambientes<5:
                #verifico la cantidad de ambientes y devuelvo un posible resultado
                impuesto = f'5% de impuesto'
            else:
                impuesto = f'35% de impuesto'
        
        return impuesto #retorno el resultado basado en el año y los ambientes
    

casa_1=Propiedad("Rivadavia",39876,"Ramos Mejia", 1946, 6)
casa_2=Propiedad("Rivadavia",40566,"Ramos Mejia", 1966, 4)
print(casa_2)
print(Propiedad.impuestoARBA(casa_1))
print(Propiedad.mayorNumeracion(casa_1,casa_2))