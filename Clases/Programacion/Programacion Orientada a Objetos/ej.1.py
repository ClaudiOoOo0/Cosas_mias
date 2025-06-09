class Cajero:

    def __init__(self, titular, numero_cuenta,):
        self.t = titular
        self.s = 100000
        self.nc = str(numero_cuenta)

    def saldo(self):
        print(f"Su saldo es ${self.s}")

    def retiro(self):
        while True:
            retiro = int(input("Ingrese la cantidad a retirar: $"))
            if retiro > self.s:
                print("La cantidad a retirar es superior al saldo disponible, vuelva a intentarlo.")
            elif retiro <= 0:
                print("Error, eliga un valor superior. ")
            else:
                self.s -= retiro
                print(f"Retiro ${retiro}, saldo total ${self.s}")
                break

    def deposito(self):
        depo = int(input("Ingrese la cantidad a depositar: $ "))
        self.s += depo
        print(f"Deposito ${depo}, saldo total ${self.s}")

    def main(self):
        while True:
            print("Bienvenido, elija su opcion:")
            print("1. Retirar saldo\n2. Agregar saldo\n3. Consultar saldo\n4. Salir.")
            opcion = int(input("\nIngrese su opcion: "))
            if opcion == 1:
                self.retiro()
            elif opcion == 2:
                self.deposito()
            elif opcion == 3:
                self.saldo()
            elif opcion == 4:
                break

saldo = 0
titular = input("Ingrese nombre del titutlar: ")
numero_cuenta = input("Ingrese numero de cuenta: ")
cajero = Cajero(titular, numero_cuenta, )
cajero.main()