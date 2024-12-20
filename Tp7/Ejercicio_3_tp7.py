"""
3. Escribir una función que devuelva la suma de los N primeros números naturales

"""

def sumar_n(n: int) -> int:
    """
    Devuelve la suma de los primeros N números naturales.

    Pre:
    - `n` debe ser un número entero mayor o igual a 0.
    
    Post:
    - Devuelve la suma de los primeros N números naturales como un número entero.
    """
    if n < 0:
        raise ValueError("El valor de n debe ser un número entero no negativo.")
    
    return (n * (n + 1)) // 2

def main():
    try:
        n = int(input("Ingrese un número N: "))
        resultado = sumar_n(n)
        print(f"La suma de los primeros {n} números naturales es: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
