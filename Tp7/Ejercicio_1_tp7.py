"""
    1. Escribir una función que devuelva la cantidad de dígitos de un número entero, sin 
    utilizar cadenas de caracteres.
"""
def cantidad_digitos(num: int) -> int:
    """
    Calcula la cantidad de dígitos de un número entero.

    Pre: 
        - El parámetro num debe ser un número entero.
        - El número puede ser positivo, negativo o cero.

    Post:
        - Devuelve la cantidad de dígitos que tiene el número absoluto (sin considerar el signo).
        - Si el número es 0, devuelve 1.
    """
    if num < 0:
        num = -num
    if num == 0:
        return 1
    return 1 + cantidad_digitos(num // 10)

def main():
    """
    Función principal para interactuar con el usuario.

    Pre: 
    - El usuario debe ingresar un número entero válido.

    Post:
    - Muestra en pantalla la cantidad de dígitos del número ingresado.
    - Maneja errores si la entrada no es válida.
    """
    try:
        num = int(input("Ingrese un numero: "))
        
        resultado = cantidad_digitos(num)
        
        print(f"La cantidad de digitos en {num} es {resultado}")
        
    except ValueError:
        print("ERROR: Por favor, ingrese un número entero válido.")
        
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    main()