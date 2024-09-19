"""
    5. Escribir funciones lambda para:
    a. Informar si un número es oblongo. Se dice que un número es oblongo cuando
    se puede obtener multiplicando dos números naturales consecutivos. Por ejemplo 6 es oblongo porque resulta de multiplicar 2 * 3.
    
    b. Informar si un número es triangular. Un número se define como triangular si
    puede expresarse como la suma de un grupo de números naturales consecutivos comenzando desde 1. Por ejemplo 10 es un número triangular porque se
    obtiene sumando 1+2+3+4.
    
    Ambas funciones lambda reciben como único parámetro el número a evaluar y devuelven True o False. No se permite utilizar ayudas externas a las mismas.
    
"""

es_oblongo = lambda n: any(n == i * (i + 1) for i in range(1, int(n ** 0.5) + 1))

es_triangular = lambda n: any(n == i * (i + 1) // 2 for i in range(1, int((2 * n) ** 0.5) + 1))

def main() -> None:
    """
    Funcion principal, donde se ingresa el numero a evalua
    """
    try:
        usuario = int(input("Ingrese el numero: "))
        
        if es_oblongo(usuario):
            print(f"El numero {usuario}, es oblongo.")
        else:
            print(F"El numero {usuario}, no es oblongo. ")
            
            
        if es_triangular(usuario):
            print(f"El numero {usuario}, es triangular")
        else:
            print(f"El numero {usuario}, no es triangular")
            
    except ValueError:
        print("ERROR, verifique que el numero sea entero.")

if __name__ == "__main__":
    main()
