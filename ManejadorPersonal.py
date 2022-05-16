from ClasePersonal import Personal
from ClaseOrganismo import Organismo
import csv

class ManejadorPersonal:
    __lista = []
    __lista2 = []

    def __init__(self):
        self.__lista = []
        self.__lista2 = []
    
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
            
        print(self.__lista[0].getNombre())
    
    def contarPersonas(self, Organismo):
        cantEdad=0
        for i in range(len(self.__lista)):
            if self.__lista[i].getNombreOrganismo() == (str(Organismo)):
                if self.__lista[i].getRiesgo() == str('Edad'):
                    cantEdad+=1
        else:
            return cantEdad
    
    def contarPersonas2(self, Organismo):
        cantEnf=0
        for i in range(len(self.__lista)):
            if self.__lista[i].getNombreOrganismo() == (str(Organismo)):
                if self.__lista[i].getRiesgo() != ('Edad'):
                    cantEnf+=1
        return cantEnf

    def Ordena(self, Org):
        for i in range(len(self.__lista)):
            if self.__lista[i].getNombreOrganismo() == (str(Org)):
                if int(self.__lista[i].getEdad()) < int(60):
                    self.__lista2.append(self.__lista[i])
        nombre = None
        for i in range(len(self.__lista2)):
            if self.__lista2[i].getNombre() > self.__lista2[i+1].getNombre():
                nombre = self.__lista2[i]
                self.__lista2[i] = self.__lista2[i-1]
                self.__lista2[i+1] = nombre
        for i in range(len(self.__lista2)): 
            print('{}'.format(self.__lista2[i].getNombre()))
                



