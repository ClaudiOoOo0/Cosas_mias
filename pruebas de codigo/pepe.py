class Cajero:

    def __init__(self, titular, numero_cuenta,):
        import os.path
        self.t = titular
        self.s = 100000
        self.nc = numero_cuenta
        id = numero_cuenta[0:3]
        self.archivo = f"cuenta{id}.txt"
        file_exist = os.path.exists(self.archivo)
        if file_exist == False:
            file = open(self.archivo,"x+")


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

while True:
    print("Bienvenido, elija su opcion:")
    print("1. Consultar saldo\n2. Agregar saldo\n3. Retirar saldo\n4. Salir.")
    opcion = int(input("\nIngrese su opcion: "))
    if opcion == 1:
        titular = input("Ingrese nombre del titutlar: ")
        numero_cuenta = input("Ingrese numero de cuenta: ")
        cuenta = Cajero(titular, numero_cuenta)
        cuenta.saldo()
    elif opcion == 2:
        cuenta.deposito()
    elif opcion == 3:
        cuenta.retiro()
    elif opcion == 4:
        break

