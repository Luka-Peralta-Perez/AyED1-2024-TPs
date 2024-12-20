"""
   4. Desarrollar una función que devuelva el producto de dos números enteros por sumas sucesivas.  
"""

def producto(n1: int, n2: int) -> int:
    """
    Devuelve el producto de dos números enteros usando sumas sucesivas.

    Pre:
        - n1, n2 deben ser enteros.

    Post:
       - Devuelve el producto de n1 y n2 calculado mediante sumas sucesivas.
    """

    resultado = 0
    
    # Manejo de números negativos
    if n2 < 0:
        for _ in range(-n2):
            resultado -= n1  # Restamos n1 en lugar de sumarlo
    else:
        for _ in range(n2):
            resultado += n1  # Sumamos n1

    return resultado

def main() -> None:
    """
    Función principal que solicita dos números al usuario y muestra su producto.
    """

    try:
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))
        
        resultado = producto(num1, num2)
        print(f"El producto de {num1} y {num2} es: {resultado}")
    except ValueError:
        print("Por favor, ingrese solo números enteros.")

if __name__ == "__main__":
    main()
    
