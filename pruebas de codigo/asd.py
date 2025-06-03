#definir clase estudiante 
class Estudiante():
    """
    Parametros para estudiante
    """

    def __init__(self, rut, nombre, apellido, edad):
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

    def notas(self):
        self.nota1 = 0
        self.nota2 = 0
        self.nota3 = 0
        self.nota4 = 0

est = Estudiante("21222602-9","Gabriel","Salazar","20")
est.describe()
