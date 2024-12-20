"""
     6. La función de Ackermann A(m,n) se define de la siguiente forma:
         n+1
         A(m-1,1)
         A(m-1,A(m,n-1))
         si m = 0
         si n = 0
         de otro modo
     Imprimir un cuadro con los valores que adopta la función para valores de m entre 0 
    y 3 y de n entre 0 y 7.
"""
def ackermann(m: int, n: int) -> int:
    """
    Calcula la función de Ackermann A(m, n).
    
    Pre:
       -m, n son enteros no negativos.
    
    Post:
        - Devuelve el valor de A(m, n) según la definición de la función de Ackermann.
    """
    # Limitar los valores de m y n para evitar desbordamiento de recursión.
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

def imprimir_cuadro_ackermann() -> None:
    """
    Imprime un cuadro con los valores de la función de Ackermann A(m, n)
    para m entre 0 y 3 y n entre 0 y 4 (limitando los valores para evitar errores).
    """
    print("Valores de la función de Ackermann:")
    for m in range(4):  # m entre 0 y 3
        fila = []
        for n in range(5):  # n entre 0 y 4
            fila.append(str(ackermann(m, n)))  # Calculamos A(m, n)
        print(" | ".join(fila))  # Imprimimos la fila del cuadro

def main() -> None:
    """
    Función principal que imprime el cuadro de la función de Ackermann.
    """
    imprimir_cuadro_ackermann()

if __name__ == "__main__":
    main()
