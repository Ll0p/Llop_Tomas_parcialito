from Consignas.Funciones import *
from Consignas.Datos import mapa

# Pedir al usuario una coordenada fila (x) entre 0 y 4 (inclusive).
# Pedir al usuario una coordenada columna (y) entre 0 y 4 (inclusive).

def main(mapa: list):
    seguir = True
    while seguir:
        fila = int(input(f'\nIngrese "x" [0-{len(mapa)-1}]: '))
        columna = int(input(f'Ingrese "y" [0-{len(mapa[0])-1}]: '))
        distancia = verificar_tesoro(mapa, fila, columna)
        if distancia != 0:
            print(f"Fallaste. El tesoro está a {distancia} casilleros de distancia.")
        else:
            print("¡Encontraste el tesoro!")
            seguir = False
main(mapa)