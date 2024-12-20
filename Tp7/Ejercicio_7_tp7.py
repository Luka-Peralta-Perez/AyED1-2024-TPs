"""
    7. Dados dos números enteros no negativos, devolver el resultado de calcular el Máximo Común Divisor (también llamado Divisor Común Mayor) basándose en las siguientes propiedades:
     MCD(X, X) = X
     MCD(X, Y) = MCD(Y, X)
     Si X > Y => MCD(X, Y) = MCD(X–Y, Y).

"""
def mcd(x: int, y: int) -> int:
    """
    Calcula el Máximo Común Divisor (MCD) de dos números enteros no negativos
    utilizando el algoritmo de Euclides basado en las propiedades de la resta sucesiva.

    Pre:
        - x, y son enteros no negativos.
    Post:
        - Devuelve el MCD de x y y.
    """
    if x == y:
        return x
    elif x > y:
        return mcd(x - y, y)
    else:
        return mcd(x, y - x)

def mcd_lista(numeros: list) -> int:
    """
    Calcula el MCD de una lista de números enteros no negativos de forma recursiva.

    Pre:
        - numeros es una lista de enteros no negativos.
    Post:
        - Devuelve el MCD de todos los elementos de la lista.
    """
    if len(numeros) == 1:
        return numeros[0]  # Si hay un solo número, su MCD es el mismo número.
    else:
        # Calcula el MCD del primer número con el MCD del resto de la lista.
        return mcd(numeros[0], mcd_lista(numeros[1:]))

def main() -> None:
    """
    Función principal para probar el cálculo del MCD de una lista de números.
    """
    try:
        # Solicitar al usuario que ingrese una lista de números enteros no negativos
        numeros = list(map(int, input("Ingrese una lista de números enteros no negativos (separados por espacios): ").split()))
        
        # Verificar que todos los números sean no negativos
        if any(num < 0 for num in numeros):
            print("Por favor, ingrese solo números enteros no negativos.")
        else:
            resultado = mcd_lista(numeros)
            print(f"El MCD de la lista {numeros} es: {resultado}")
    except ValueError:
        print("Por favor, ingrese solo números enteros válidos.")

if __name__ == "__main__":
    main()