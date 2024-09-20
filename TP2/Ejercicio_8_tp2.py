""""
    8. Utilizar la técnica de listas por comprensión para construir una lista con todos los
    números impares comprendidos entre 100 y 200.
"""


def impares():
    """Genera una lista de números impares entre 100 y 200."""
    return [x for x in range(101, 201) if x % 2 != 0]

def main():
    """Funcion principal"""
    print(impares())
    return None

if __name__ == "__main__":
    main()
    
    