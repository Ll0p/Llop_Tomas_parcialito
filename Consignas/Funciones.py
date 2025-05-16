'''verificar_tesoro(mapa: list, x: int, y: int) -> int
La función debe retornar:
    - 0 si el usuario encontró el tesoro.
    - En caso contrario, retornar la distancia Manhattan entre la coordenada ingresada y la ubicación real del
tesoro.
**Distancia Manhattan**:
distancia = |x_usuario - x_tesoro| + |y_usuario - y_tesoro|
Según el valor retornado, mostrar al usuario:
    - "¡Encontraste el tesoro!" si retorna 0.
    - "Fallaste. El tesoro está a X casilleros de distancia." si retorna otro número.
El juego continúa hasta que el usuario encuentre el tesoro o hasta que el usuario lo desee.
Nota: No se pueden utilizar funciones propias.'''

def verificar_tesoro(mapa: list, x: int, y: int) -> int:
    fila_t = None
    colum_t = None
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] != 0:
                fila_t = i
                colum_t = j
                break
        if fila_t != None:
            break
    
    if mapa[x][y] == 0:
        if x == colum_t and y == fila_t:
            distancia = (x + colum_t) - (y + fila_t)
        else:
            distancia = (x - fila_t) + (y - colum_t)
            if distancia < 0:
                distancia *= -1
    else:
        distancia = 0
    return distancia