"""
    2. Desarrollar una función que reciba un número binario y lo devuelva convertido a 
    base decimal. 
"""
def convertir_numero(numero: int, tipo: str) -> int:
    """
    Convierte un número entre binario y decimal según el tipo indicado.
    
    Pre:
    - `numero` debe ser un número entero, que puede ser en base binaria o decimal.
    - `tipo` debe ser un string que indique el tipo de conversión:
      - "binario_a_decimal" para convertir de binario a decimal.
      - "decimal_a_binario" para convertir de decimal a binario.
    
    Post:
    - Devuelve el número convertido según el tipo indicado.
    
    Args:
        numero (int): El número que se va a convertir, que puede ser en formato binario o decimal.
        tipo (str): El tipo de conversión ("binario_a_decimal" o "decimal_a_binario").
    
    Returns:
        int: El número convertido al formato adecuado.
    """
    if tipo == "binario_a_decimal":
        # Convierte binario a decimal
        def binario_a_decimal(binario, position=0):
            if binario == 0:
                return 0
            ultimo_digito = binario % 10
            numero_decimal = ultimo_digito * (2 ** position)
            return numero_decimal + binario_a_decimal(binario // 10, position + 1)

        return binario_a_decimal(numero)

    elif tipo == "decimal_a_binario":
        # Convierte decimal a binario
        def decimal_a_binario(decimal):
            if decimal == 0:
                return 0
            return decimal % 2 + 10 * decimal_a_binario(decimal // 2)

        return decimal_a_binario(numero)

    else:
        raise ValueError("El tipo de conversión debe ser 'binario_a_decimal' o 'decimal_a_binario'")


def menu() -> None:
    """
    Función principal que permite al usuario ingresar un número binario o decimal y elegir el tipo de conversión.
    
    Pre:
    - Esta función no recibe parámetros.
    
    Post:
    - Esta función no devuelve valores. Solicita un número al usuario y muestra el resultado de la conversión.
    """
    while True:
        try:
            # Ingreso de número
            numero = int(input("Ingrese un número (binario o decimal): "))
            tipo = input("Ingrese el tipo de conversión (binario_a_decimal o decimal_a_binario): ").strip().lower()
            
            if tipo not in ["binario_a_decimal", "decimal_a_binario"]:
                print("Error: Tipo de conversión inválido. Debe ser 'binario_a_decimal' o 'decimal_a_binario'.")
                continue

            # Mostrar el resultado de la conversión
            resultado = convertir_numero(numero, tipo)
            print(f"El resultado de la conversión es: {resultado}")
            break
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    menu()
def convertir_numero(numero: int, tipo: str) -> int:
    """
    Convierte un número entre binario y decimal según el tipo indicado.
    
    Pre:
    - `numero` debe ser un número entero, que puede ser en base binaria o decimal.
    - `tipo` debe ser un string que indique el tipo de conversión:
      - "binario_a_decimal" para convertir de binario a decimal.
      - "decimal_a_binario" para convertir de decimal a binario.
    
    Post:
    - Devuelve el número convertido según el tipo indicado.
    
    Args:
        numero (int): El número que se va a convertir, que puede ser en formato binario o decimal.
        tipo (str): El tipo de conversión ("binario_a_decimal" o "decimal_a_binario").
    
    Returns:
        int: El número convertido al formato adecuado.
    """
    if tipo == "binario_a_decimal":
        # Convierte binario a decimal
        def binario_a_decimal(binario, position=0):
            if binario == 0:
                return 0
            ultimo_digito = binario % 10
            numero_decimal = ultimo_digito * (2 ** position)
            return numero_decimal + binario_a_decimal(binario // 10, position + 1)

        return binario_a_decimal(numero)

    elif tipo == "decimal_a_binario":
        # Convierte decimal a binario
        def decimal_a_binario(decimal):
            if decimal == 0:
                return 0
            return decimal % 2 + 10 * decimal_a_binario(decimal // 2)

        return decimal_a_binario(numero)

    else:
        raise ValueError("El tipo de conversión debe ser 'binario_a_decimal' o 'decimal_a_binario'")


def menu() -> None:
    """
    Función principal que permite al usuario ingresar un número binario o decimal y elegir el tipo de conversión.
    
    Pre:
    - Esta función no recibe parámetros.
    
    Post:
    - Esta función no devuelve valores. Solicita un número al usuario y muestra el resultado de la conversión.
    """
    while True:
        try:
            # Ingreso de número
            numero = int(input("Ingrese un número (binario o decimal): "))
            tipo = input("Ingrese el tipo de conversión (binario_a_decimal o decimal_a_binario): ").strip().lower()
            
            if tipo not in ["binario_a_decimal", "decimal_a_binario"]:
                print("Error: Tipo de conversión inválido. Debe ser 'binario_a_decimal' o 'decimal_a_binario'.")
                continue

            # Mostrar el resultado de la conversión
            resultado = convertir_numero(numero, tipo)
            print(f"El resultado de la conversión es: {resultado}")
            break
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    menu()
