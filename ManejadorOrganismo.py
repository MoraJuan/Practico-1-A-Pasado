
from ClaseOrganismo import Organismo
from ClasePersonal import Personal
import csv
from ManejadorPersonal import ManejadorPersonal

class ManejadorOrganismo:
    __lista = []

    def __init__(self):
        self.__lista = []
    
    def cargaLista(self):
        archivo = open('Organismos-del-Estado.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera=True
        for fila in reader: 
            if bandera:
                bandera = False
            else:
                UnOrganismo = Organismo(fila[0], fila[1], fila[2], fila[3])
                self.__lista.append(UnOrganismo)
        print('a')
    
    def contar(self):
        for i in range(len(self.__lista)):
            print('{}'.format(self.__lista[i].getNombre))
            print('{}'.format(ManejadorPersonal.contarPersonas()))
            print('{}'.format(ManejadorPersonal.contarPersonas2()))


