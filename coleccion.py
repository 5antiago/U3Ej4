import numpy as np 
from datetime import datetime
from Empleado import Empleado
from EmpleadoPlanta import EmpleadoPlanta
from Empleadocontratado import EmpleadoContratado
from EmpleadoExterno import EmpleadoExterno

class coleccion(object):
    __Empleados= None
    __count = int

    def __init__(self, tam):
        self.__Empleados = np.empty(tam, dtype=Empleado)
        self.__count = 0
    def agregarempleado(self, empleado):
        self.__Empleados[self.__count] = empleado
        self.__count +=1
    def incrementarhoras(self, dni, horas):
        i = 0
        flag = True
        while i<len(self.__Empleados) and flag:
            if type(self.__Empleados[i]) == EmpleadoContratado and self.__Empleados[i].getdni() == dni:
                self.__Empleados[i].registrarhoras(horas)
                flag = False
            i += 1
        return flag
    def ayuda(self): 
        aux=""
        for empleado in self.__Empleados:
            if empleado.Sueldo() < 25000:
                aux+="\n - {0:15} {1:10} {2:8}".format(empleado.getnom(), empleado.getdir(), empleado.getdni())
        return aux
    def Sueldos(self):
        aux = ""
        for empleado in self.__Empleados:
            aux+="- {0:15} \t {1:10} \t {2:.2f} \n".format(empleado.getnom(), empleado.gettel(),empleado.Sueldo())
        return aux
    def tareasapagar(self, tarea):
        acum = 0
        for empleado in self.__Empleados:
            if isinstance(empleado, EmpleadoExterno):
                if empleado.gettarea() == tarea and empleado.getfinal() > datetime.now() :
                    acum += empleado.getcostoobra()
        return acum
