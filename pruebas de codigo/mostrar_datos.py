import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

lista_medicamentos= []

class Farmacia:
    def __init__(self, nombre, componente_principal, laboratorio, marca, tipo, precio):
        self.nombre=nombre
        self.componente_principal=componente_principal
        self.laboratorio=laboratorio
        self.marca=marca
        self.tipo=tipo
        self.precio=precio

    def guardar_medicamentos(self):
        """
        Se crea una lista con los datos del medicamento
        """
        nuevo_med = (self.nombre, self.componente_principal, self.laboratorio, self.marca, self.tipo, self.precio)
        lista_medicamentos.append(nuevo_med)
    
    def mostrar_medicamentos(self, lista_medicamentos):
        for mos in lista_medicamentos:
            print(f"Nombre: {mos[0]}\nComponente principal: {mos[1]}\nLaboratorio: {mos[2]}\n Marca: {mos[3]}\nTipo: {mos[4]}\nPrecio: {mos[5]}")
            

#nose pa que sirve
"""     df = pd.DataFrame(lista_medicamentos, columns=['Nombre', 'Componente Principal', 'Laboratorio', 'Marca', 'Tipo', 'Precio'])"""

class Comprador:
    def __init__(self, rut="", primer_nombre="", segundo_nombre="", apellido_paterno="", apellido_materno="",monto_a_pagar=0):
        self.rut=rut
        self.primer_nombre=primer_nombre
        self.segundo_nombre=segundo_nombre
        self.apellido_paterno=apellido_paterno
        self.apellido_materno=apellido_materno
        self.monto_a_pagar=monto_a_pagar


#Menu
def menu():
    while True:
        print("BIENVENIDO A LA FARMACIA\n INGRESE LA OPCION DESEADA: ")
        print("1-Ingresar datos de los medicamentos")
        print("2-Ingresar datos de las personas que compran")
        print("3-Visualizar datos de los medicamentos ")
        print("4-Visualizar datos de las personas que compran")
        print("5-Visualizar gráfico del monto a pagar por las personas que compraron medicamentos")
        print("6-Salir del programa")
        opcion= int(input("Ingrese la opción que desee: "))
        if opcion == 1:
            print("\nIngrese los datos de los medicamentos\n")
            nombre_producto = input("Nombre: ")
            componente_principal = input("Componente principal: ")
            laboratorio = input("Laboratorio: ")
            marca = input("Marca: ")
            tipo = input("Tipo: ")
            precio = int(input("Precio: "))
            med = Farmacia(nombre_producto, componente_principal, laboratorio, marca, tipo, precio,)
            med.guardar_medicamentos()
        
        elif opcion == 3:
            mos = Farmacia(lista_medicamentos, componente_principal, laboratorio, marca, tipo, precio)
            mos.mostrar_medicamentos(lista_medicamentos)
            #Se usa la segunda clase, haces algo similar a la opcion 1

menu()
