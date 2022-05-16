from ManejadorPersonal import ManejadorPersonal
from ManejadorOrganismo import ManejadorOrganismo

if __name__ == '__main__':
    Obj = ManejadorPersonal()
    Obj2 = ManejadorOrganismo()

    Obj.cargaLista()
    Obj2.cargaLista()
    Obj2.contar(Obj)
    Org = input('Ingrese organizacion: ')
    Obj.Ordena(Org)