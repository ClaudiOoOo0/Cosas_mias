lista_medicamentos= []
nombre = input("Nombre: ")
componente_principal = input("Componente: ")
laboratorio = input("Laboratorio: ")
marca = input("Marca: ")
tipo = input("Tipo: ")
precio = int(input("Precio: "))

nuevo_med = (nombre, componente_principal, laboratorio, marca, tipo, precio)
lista_medicamentos.append(nuevo_med)

print("Hola")