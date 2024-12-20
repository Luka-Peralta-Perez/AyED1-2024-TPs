"""
    5. Realizar una función que devuelva el resto de dos números enteros, utilizando restas sucesivas.
"""

def resto_numeros(numero1: int, numero2: int) -> int:
    """
    Esta función devuelve el resto de la división de dos números enteros utilizando restas sucesivas.

    Pre:
        - numero1, numero2 deben ser enteros y numero2 no puede ser cero.

    Post:
        - Devuelve el resto de la división de numero1 entre numero2 calculado por restas sucesivas.
    """
    if numero2 == 0:
        raise ValueError("El divisor no puede ser cero.")

    while numero1 >= numero2:
        numero1 -= numero2  # Restamos el divisor de numero1 sucesivamente.

    return numero1  # El resto será el valor de numero1 cuando ya no se pueda restar más.


def main() -> None:
    """
    Función principal que solicita dos números enteros al usuario
    y muestra el resto de su división utilizando la función resto_numeros.
    """
    try:
        numero1 = int(input("Ingrese el primer número entero: "))
        numero2 = int(input("Ingrese el segundo número entero: "))

        resto = resto_numeros(numero1, numero2)
        print(f"El resto de {numero1} dividido por {numero2} es: {resto}")

    except ValueError as e:
        print(f"Error: {e}. Por favor, ingrese solo números enteros.")
        
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()

    