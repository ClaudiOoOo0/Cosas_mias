#definir clase estudiante 
class Estudiante():
    """
    Parametros para estudiante
    """

    def __init__(self, rut = "00000000-0", nombre = "Estudiante", apellido = "Estudioso", edad = 0):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def describe(self):
        print(f"""Estudiante:
        Rut: {self.rut}
        Nombre: {self.nombre} {self.apellido}
        Edad: {self.edad}
        """)

est = Estudiante()
est.describe()
est2 = Estudiante("21222602-9","Gabriel","Salazar","20")
est2.describe()