"""
    9. Realizar una función recursiva para imprimir una matriz de M x N con el formato 
    apropiado.
"""

def imprimir_matriz(matriz, fila=0):
    """
    Imprime una matriz de M x N de forma recursiva.

    Pre:
        - matriz es una lista de listas que representa la matriz.
        - fila es el índice de la fila actual que se está imprimiendo.

    Post:
        - Imprime la matriz en el formato apropiado.
    """
    
    if fila == len(matriz):
        return
    
    # Imprimir la fila actual
    print(" ".join(map(str, matriz[fila])))
    
    # Llamar recursivamente para la siguiente fila
    imprimir_matriz(matriz, fila + 1)

def main() -> None:
    """
    Función principal para probar la impresión de la matriz.
    """
    # Definir una matriz de ejemplo
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("La matriz es:")
    imprimir_matriz(matriz)

if __name__ == "__main__":
    main()
    