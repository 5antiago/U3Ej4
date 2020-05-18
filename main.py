from datetime import date
from datetime import datetime
import csv
from menu import Menu
from coleccion import coleccion
from Empleadocontratado import EmpleadoContratado
from EmpleadoPlanta import EmpleadoPlanta
from EmpleadoExterno import EmpleadoExterno

if __name__ == "__main__":
    empleados = coleccion(int(input("Ingrese cantidad de empleados: ")))
    with open("planta.csv") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            empleados.agregarempleado(EmpleadoPlanta(row[1],row[0], row[2], row[3], int(row[4]), int(row[5])))
    with open("contratados.csv") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            empleados.agregarempleado(EmpleadoContratado(row[1],row[0], row[2], row[3], 
            datetime.strptime(row[4], "%d/%m/%Y"), datetime.strptime(row[5], "%d/%m/%Y"), int(row[6]) ))
    with open("externos.csv") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            empleados.agregarempleado(EmpleadoExterno(row[1],row[0], row[2], row[3], row[4], 
            datetime.strptime(row[5], "%d/%m/%Y"), datetime.strptime(row[6], "%d/%m/%Y"), float(row[7]), float(row[8]), float(row[9]) ))
    EmpleadoContratado.cambiarvalorhora(float(input("Ingrese El valor de la hora para empleados contratados: ")))

    menu = Menu()
    print(" 1. Registrar Horas \n 2. Total de la tarea \n 3. Ayuda a empleados \n 4. Sueldos \n 0. Salir")
    op = int(input("\n Ingrese opcion: "))
    while op > 0:
        menu.opcion(op,empleados)
        print(" 1. Registrar Horas \n 2. Total de la tarea \n 3. Ayuda a empleados \n 4. Sueldos \n 0. Salir")
        op = int(input("\n Ingrese opcion: "))