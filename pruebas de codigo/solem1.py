""""""
import math
a = 0
b = 0
c = 0
def ecuacion(a, b, c):
    a = int(input("Ingrese el valor de a : "))
    b = int(input("Ingrese el valor de b : "))
    c = int(input("Ingrese el valor de c : "))
    
    raiz = b**2 -4*a*c
    if raiz > 0:
        x1 = (-b + raiz**0.5) / (2*a)
        x2 = (-b - raiz**0.5) / (2*a)
        print(x1)
        print(x2)
    else:
        print("Error")
    return x1, x2

ecuacion(a,b,c)