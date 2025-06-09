class Ventas:
    def __init__(self, nombre_vendedor, precio_articulo, monto_comision=0):
        self.nombre_v = nombre_vendedor
        self.precio_a = precio_articulo
        self.monto_com = monto_comision
    
    def objeto(self):

        return 0


while True:
    print("1.- Ingreso de datos y creación del objeto\n2.- Calcular comisión\n3.- Mostrar datos (estado) del objeto\n4.- Salir\n")
    opcion = int(input("Seleccione su opcion: "))
    if opcion == 1:
        nombre_vendedor = input("Ingrese el nombre del vendedor")
        precio_articulo = input("Ingrese precio del articulo: ")
        obj = Ventas(nombre_vendedor, precio_articulo)