class Personal:
    __nombre = None
    __apellido = None
    __dni = None
    __edad = None
    __direccion = None
    __telefono = None
    __riesgo = None
    __nombreOrganismo = None

    def __init__(self, nombre, apellido, dni, edad, direccion, telefono,riesgo,nombreOrganismo):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__direccion = direccion
        self.__dni = dni
        self.__edad = edad
        self.__telefono = telefono
        self.__riesgo =riesgo
        self.__nombreOrganismo = nombreOrganismo

    def getApellidos(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getDni(self):
        return self.__dni
    def getEdad(self):
        return self.__edad
    def getTelefono(self):
        return self.__telefono
    def getNombreOrganismo(self):
        return self.__nombreOrganismo
    def getRiesgo(self):
        return self.__riesgo