#"- {0:15} \t {1:10} \t {2:5.2}"
from coleccion import coleccion

class Menu(object):
    __switcher = dict
    def __init__(self):
        self.__switcher = {1: self.Registrar, 2: self.Totaltarea, 3: self.ayuda, 4:self.Sueldos}
    def opcion(self, op, empleados):
        self.__switcher.get(op, lambda a: print("Opcion Incorrecta"))(empleados)

    def Registrar(self, empledos):
        if not empledos.incrementarhoras(input("Ingrese DNI: "), int(input("Ingrese Horas a incrementar: "))):
            print("Horas Registradas")
        else:
            print("No se encontro el Empleado")
    def Totaltarea(self, empledos):
        aux=empledos.tareasapagar(input("Ingrese Tarea: "))
        if aux !=0:
            print("El monto a pagar es: {:.2f}".format(aux))
        else:
            print("No se encontraron montos a pagar para la tarea")
    def ayuda(self, empledos):
        aux = empledos.ayuda()
        if aux != "":
            print(aux)
        else:
            print("No ha empleados que califiquen para la ayuda")
    def Sueldos(self, empledos):
        print(empledos.Sueldos())
