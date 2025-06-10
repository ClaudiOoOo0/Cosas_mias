import seaborn as sns
#import pandas as pd
import matplotlib.pyplot as plt

#Listas globales
lista_medicamentos= []
lista_comprador= []

#Clase de los medicamentos
class Farmacia:
    def __init__(self, nombre, componente_principal, laboratorio, marca, tipo, precio):
        self.nombre = nombre
        self.componente_principal = componente_principal
        self.laboratorio = laboratorio
        self.marca = marca
        self.tipo = tipo
        self.precio = precio

    def guardar_medicamentos(self):
        """
        Se crea una lista con los datos del medicamento.
        """
        nuevo_med = (self.nombre, self.componente_principal, self.laboratorio, self.marca, self.tipo, self.precio)
        lista_medicamentos.append(nuevo_med)
    
    def mostrar_medicamentos(self, lista_medicamentos):
        """
        Muestra la o las listas de medicamentos.
        """
        for mos in lista_medicamentos:
            print(f"\nNombre: {mos[0]}\nComponente principal: {mos[1]}\nLaboratorio: {mos[2]}\nMarca: {mos[3]}\nTipo: {mos[4]}\nPrecio: {mos[5]}\n")



class Comprador:
    def __init__(self, rut="", primer_nombre="", segundo_nombre="", apellido_paterno="", apellido_materno="",monto_a_pagar=0):
        self.rut = rut
        self.primer_nombre = primer_nombre
        self.segundo_nombre = segundo_nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.monto_a_pagar = monto_a_pagar

    def guardar_datos_comprador(self):
        """
        Se crea una lista con los datos del comprador.
        """
        #Las listas seran globales
        nuevo_com = (self.rut, self.primer_nombre, self.segundo_nombre, self.apellido_paterno, self.apellido_materno, self.monto_a_pagar)
        lista_comprador.append(nuevo_com)
    
    def mostrar_datos_comprador(self, lista_comprador):
        """
        Muestra la o las listas dde compradores.
        """
        #Se imprime cada dato del comprador
        for data_co in lista_comprador:
            print(f"\nRut: {data_co[0]}\nPrimer Nombre: {data_co[1]}\nSegundo Nombre: {data_co[2]}\nApellido Paterno: {data_co[3]}\nApellido Materno: {data_co[4]}\nMonto a Pagar: {data_co[5]}\n")


#Menu
while True:
    print("SISTEMA DE VENTA DE MEDICAMENTOS")
    print("1-Ingresar datos de los medicamentos")
    print("2-Ingresar datos de las personas que compran")
    print("3-Visualizar datos de los medicamentos ")
    print("4-Visualizar datos de las personas que compran")
    print("5-Visualizar gráfico del monto a pagar por las personas que compraron medicamentos")
    print("6-Salir del programa")
    opcion= int(input("Seleccione su opcion: "))
    if opcion == 1:
        print("\nIngrese los datos de los medicamentos\n")
        nombre_producto = input("Nombre: ")
        componente_principal = input("Componente principal: ")
        laboratorio = input("Laboratorio: ")
        marca = input("Marca: ")
        #comprobacion tipo de medicamento
        tipo = input("Tipo de medicamento:\n-Capsula\n-Suspencion\n-Inyecion\nTipo: ")
        if tipo == "Capsula" or "capsula" or "Suspencion" or "suspencion" or "Inyecion" or "inyecion":
            print("Tipo de medicamento aceptado")
        else:
            print("Tipo de medicamento no aceptado, por favor ingrese Capsula, Suspencion o Inyecion")
        precio = int(input("Precio: "))
        if precio == 0:
            print("El precio no puede ser 0, por favor ingrese un precio valido")
        elif precio < 0:
            print("El precio no puede ser negativo, por favor ingrese un precio valido")
        med = Farmacia(nombre_producto, componente_principal, laboratorio, marca, tipo, precio)
        med.guardar_medicamentos()
    
    elif opcion == 2:
        print("\nIngrese los datos del comprador\n")
        rut = input("Rut: ")
        primer_nombre = input("Ingrese el primer nombre: ")
        segundo_nombre = input("Ingrese el segundo_nombre: ")
        apellido_paterno = input("Ingrese el apellido paterno: ")
        apellido_materno = input("Ingrese el apellido materno: ")
        #Hacer comprobacion si el monto a pagar es similar a algunos de los medicamentos en lista
        monto_a_pagar = int(input("Ingrese monto a pagar: "))
        precios_disponibles = [med[5] for med in lista_medicamentos]
        if monto_a_pagar in precios_disponibles:
            com = Comprador(rut, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno, monto_a_pagar)
            com.guardar_datos_comprador()
            print(" ")

    elif opcion == 3:
        mos = Farmacia(lista_medicamentos, componente_principal, laboratorio, marca, tipo, precio)
        mos.mostrar_medicamentos(lista_medicamentos)
#MODIFICAR ESTA OPCION PARA QUE MUESTRE LOS MEDICAMENTOS

    elif opcion == 4:
        #similar a la opcion 3
        data_co = Comprador(lista_comprador)
        data_co.mostrar_datos_comprador(lista_comprador)
    #GRAFICO

    elif opcion == 5:
        x=[2, 5.6, 10, 1.2, 40, 5.6]
        y=["hHector", "paula", "pepe", "maria", "cynthia", "xdddd"]
        plt.bar(y, x, color="red", edgecolor="b")
        plt.title("grafico de notas")
        plt.xlabel("estudiantes")
        plt.ylabel("notas de matematicas")
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.show()
