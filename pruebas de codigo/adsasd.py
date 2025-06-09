"""
Crea un programa en python con una sola clase para convertir moneda
primero pide el cambio de moneda luego el valor observador si es compra
vale 5% mas del observado si es venta vale %6 mas del observado.
ᾟConversión de monedas a CLP
1. Dólar (USD)
2. Real Brasileño (BRL)
3. Yuan Chino (CNY)
4. Sol Peruano (PEN)
5. Peso Argentino (ARS)
Seleccione la moneda a cambiar (1-5): 1
Ingrese el valor observado actual de 1 USD (Dólar): 900
Ingrese la operación (C para Compra, V para Venta): C
Ingrese la cantidad en USD: 100
ᾟCompra: 100 USD equivale a CLP 83700.0
ᾟOperación finalizada con Dólar (USD). Gracias por usar el sistema.

"""
class Conversor():

    def __init__(self, opcion, valor_obs, compra_venta, cantidad):
        self.opcion = opcion
        self.valor_obs = valor_obs
        self.compra_venta = compra_venta
        self.cantidad = cantidad

    
    def valor(self):
        if self.compra_venta == "c" or "C":
            self.compra_venta = 1.05
            #agregar un 5% +
        elif compra_venta == "v" or "V":
            compra_venta = 1.06
            #agregar un 6% +
        

def opciones(opcion):
    if opcion == 1:
        opcion = "Dolar"
    elif opcion == 2:
        opcion = "Real Brasileño"
    elif opcion == 3:
        opcion = "Yuan Chino"
    elif opcion == 4:
        opcion = "Sol Peruano"
    elif opcion == 5:
        opcion = "Peso Argentino"
    return opcion

#menu pendejo
print("Conversor de monedas a CLP")
print("\n1. Dólar (USD)\n2. Real Brasileño (BRL)\n3. Yuan Chino (CNY)\n4. Sol Peruano (PEN)\n5. Peso Argentino (ARS)")
opcion = int(input(f"Seleccione la moneda a cambiar (1-5): "))
opcion = opciones(opcion)
#Agregar el tipo de moneda segun la opcion escogida
valor_obs = float(input(f"Ingrese el valor observado actual de 1 {opcion}: "))
#Vale 5% mas del observado si es venta vale %6 mas del observado.
compra_venta = input("Ingrese la operación (C para Compra, V para Venta): ")
#Lo mismo
cantidad = int(input(f"Ingrese la cantidad en {"tipo de moneda"}: "))

convertir = Conversor(opcion, valor_obs, compra_venta, cantidad)
convertir.valor()
 
