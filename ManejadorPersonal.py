from ClasePersonal import Personal
from ClaseOrganismo import Organismo
import csv

class ManejadorPersonal:
    __lista = []

    def __init__(self):
        self.__lista = []
    
    def cargaLista(self):
        archivo = open('Personal-exceptuado.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                UnPersonal = Personal(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7])
                self.__lista.append(UnPersonal)
            
        print('{}'.format(self.__lista[1].getNombre()))
    
    def contarPersonas(self):
        cantEdad=0
        for i in range(len(self.__lista)):
            if self.__lista[i].getRiesgo() == str('Edad'):
                cantEdad+=1
        return cantEdad
    
    def contarPersonas2(self):
        cantEnf=0
        for i in range(len(self.__lista)):
            if self.__lista[i].getRiesgo() != str('Edad'):
                cantEnf+=1
        return cantEnf
               
       