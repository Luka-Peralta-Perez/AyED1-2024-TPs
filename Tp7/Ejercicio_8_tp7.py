"""
    8. Realizar la implementación recursiva del método de selección para ordenar una lista 
    de números enteros. Sugerencia: Colocar el elemento más pequeño en la primera 
    posición, y luego ordenar el resto de la lista con una llamada recursiva. No usar las 
    funciones min() ni max() de Python.
"""
def encontrar_indice_minimo(lista: list, inicio: int) -> int:
    """
    Encuentra el índice del elemento más pequeño en la lista a partir de un índice de inicio.

    Pre:
        - lista es una lista de números enteros.
        - inicio es el índice desde el cual se comienza a buscar el mínimo.

    Post:
        - Devuelve el índice del elemento más pequeño en la lista.
    """
    if inicio == len(lista) - 1:  # Si estamos en el último elemento
        return inicio
    
    # Encuentra el índice del mínimo en el resto de la lista
    indice_minimo_resto = encontrar_indice_minimo(lista, inicio + 1)
    
    if lista[inicio] < lista[indice_minimo_resto]:
        return inicio
    else:
        return indice_minimo_resto

def seleccion_recursiva(lista: list) -> list:
    """
    Ordena una lista de números enteros utilizando el método de selección de forma recursiva.

    Pre:
        - lista es una lista de números enteros.

    Post:
        - Devuelve una nueva lista ordenada.
    """
    if len(lista) == 0:  
        return []
    
 
    indice_minimo = encontrar_indice_minimo(lista, 0)
    
  
    lista[0], lista[indice_minimo] = lista[indice_minimo], lista[0]
    
    # Ordena recursivamente el resto de la lista
    resto_ordenado = seleccion_recursiva(lista[1:])
    
    # Devuelve la lista ordenada
    return [lista[0]] + resto_ordenado

def main() -> None:
    """
    Función principal para probar el método de selección recursivo.
    """
    try:
        numeros = list(map(int, input("Ingrese una lista de números enteros (separados por espacios): ").split()))
        
        lista_ordenada = seleccion_recursiva(numeros)
        
        print(f"Lista ordenada: {lista_ordenada}")
        
    except ValueError:
        print("Por favor, ingrese solo números enteros válidos.")

if __name__ == "__main__":
    main()