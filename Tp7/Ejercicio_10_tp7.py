"""
  10.Escribir una función que sume todos los elementos de una matriz de M x N y de
    vuelva el resultado. No usar la función sum().                                                                                                                          
"""
def sumar_matriz(matriz, fila=0, columna=0):
    # Caso base: Si hemos recorrido todas las filas, terminamos
    if fila == len(matriz):
        return 0
    
    # Caso base: Si hemos recorrido todas las columnas de la fila actual, pasamos a la siguiente fila
    if columna == len(matriz[fila]):
        return sumar_matriz(matriz, fila + 1, 0)
    
    # Sumar el valor actual y la llamada recursiva para la siguiente columna
    return matriz[fila][columna] + sumar_matriz(matriz, fila, columna + 1)

# Ejemplo de uso:
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = sumar_matriz(matriz)
print("La suma de todos los elementos es:", resultado)
