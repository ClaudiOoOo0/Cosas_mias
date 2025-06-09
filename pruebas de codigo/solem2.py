evaluacion = []
promedio = 0
jugadores = 0

def registrar_rendimiento(evaluacion, jugadores):
    for i in range(jugadores):
        rendimiento = int(input(f"Ingrese el rendimiento del jugador {i+1} : "))
        evaluacion.append(rendimiento)
    return evaluacion, jugadores

def obtener_promedio(evaluacion, promedio, jugadores):
    suma = sum(evaluacion)
    promedio = suma / jugadores
    round(promedio,2)
    return promedio

def detectar_anomalias(evaluacion, promedio):
    return

def main():
    print("Bienvenido.")
    jugadores = int(input("Ingrese la cantidad de jugadores: "))
    registrar_rendimiento(evaluacion, jugadores)
    obtener_promedio(evaluacion, promedio, jugadores)
    detectar_anomalias(evaluacion, promedio)



main()







