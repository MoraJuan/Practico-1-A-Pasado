class Organismo:
    __nombre = None
    __domicilio = None
    __localidad = None
    __telefono = None

    def __init__(self, nombre, domicilio, localidad ,telefono):
        self.__nombre = nombre
        self.__domicilio = domicilio
        self.__localidad = localidad
        self.__telefono = telefono
    
    def getNombre(self):
        return self.__nombre
    def getDomicilio(self):
        return self.__domicilio
    def getTelefono(self):
        return self.__telefono
    def getLocalidad(self):
        return self.__localidad
        