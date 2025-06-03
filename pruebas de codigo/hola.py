"""
Ejercicio 1: Clase Coche (Básico)
Crea una clase llamada Coche con los siguientes atributos y métodos:

Atributos:
marca (string)
modelo (string)
año (entero)
velocidad (entero, inicializado en 0)
Métodos:
_init_(self, marca, modelo, año): El constructor para inicializar los atributos.
acelerar(self, incremento): Aumenta la velocidad en incremento.
frenar(self, decremento): Disminuye la velocidad en decremento, asegurándote de que la velocidad nunca sea negativa.
obtener_info(self): Devuelve una cadena con la información completa del coche (marca, modelo, año y velocidad actual).
Instrucciones:

Crea una instancia de la clase Coche.
Acelera el coche varias veces.
Frena el coche.
Imprime la información del coche.
"""

class coche():
    """
    Se describe el tipos de vehiculo
    """

    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def describe(self):
        print("\nDesripcion del vehiculo:\n")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")

marca = input("\nMarca del auto: ")
modelo = input("Modelo del auto: ")
año = int(input("Año del auto: "))
auto = coche(marca, modelo, año)
auto.describe()




