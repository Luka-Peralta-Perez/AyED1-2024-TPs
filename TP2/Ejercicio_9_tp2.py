"""
    9. Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7
    que no sean múltiplos de 5. A y B se ingresar desde el teclado. 
"""
from typing import List
def multiplos(a: int, b: int) -> List[int]:
    return [x for x in range(a, b) if x % 7 == 0 and x % 5!=0]

def main() -> None:
    try:
        a = int(input("Ingrese el rango de a: "))
        b = int(input("Ingrese el rango de b: "))

        numeros = multiplos(a, b)
        print(f"Los numeros multiplos de 7 son: {numeros}")
        
    except ValueError:
        print("ERROR: Los numeros ingresados deben ser enteros positivos. ")

if __name__ == "__main__":
    main()
    
    
