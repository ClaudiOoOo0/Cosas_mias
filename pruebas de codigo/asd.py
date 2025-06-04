#definir clase estudiante 
class Estudiante():
    """
    Parametros para estudiante
    """

    def __init__(self, rut, nombre, apellido, edad, nota1, nota2, nota3, nota4, promfinal):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.promfinal = promfinal

    def describenota(self):
        print(f"""\nEstudiante:
        Rut: {self.rut}
        Nombre: {self.nombre} {self.apellido}
        Edad: {self.edad}
        Notas: {self.nota1}, {self.nota2}, {self.nota3}, {self.nota4}
        Promedio: {round(self.promfinal, 3)}
        """)


nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
nota4 = float(input("Ingrese la nota 4: "))

prom1 = nota1 * 0.15 
prom2 = nota2 * 0.20
prom3 = nota3 * 0.25
prom4 = nota4 * 0.40
promfinal = prom1 + prom2 + prom3 + prom4

notas = Estudiante("21222602-9","Gabriel","Salazar","20", nota1, nota2, nota3, nota4, promfinal)
notas.describenota()

