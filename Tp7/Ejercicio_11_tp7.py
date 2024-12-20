"""
    11.Desarrollar una función que devuelva el mínimo elemento de una matriz de M x N.
"""

def minimo_matriz(matriz, fila=0, columna=0, minimo=float('inf')):
    # Caso base: Si hemos recorrido todas las filas, devolvemos el mínimo encontrado
    if fila == len(matriz):
        return minimo
    
    # Caso base: Si hemos recorrido todas las columnas de la fila actual, pasamos a la siguiente fila
    if columna == len(matriz[fila]):
        return minimo_matriz(matriz, fila + 1, 0, minimo)
    
    # Actualizamos el mínimo si encontramos un valor más pequeño
    nuevo_minimo = min(minimo, matriz[fila][columna])
    
    # Llamada recursiva para la siguiente columna
    return minimo_matriz(matriz, fila, columna + 1, nuevo_minimo)

# Ejemplo de uso:
matriz = [
    [3, 5, 7],
    [9, 2, 6],
    [8, 1, 4]
]

resultado = minimo_matriz(matriz)
print("El mínimo elemento de la matriz es:", resultado)
