"""
    6. Escribir una función que reciba una lista de números enteros como parámetro y la
    normalice, es decir que todos sus elementos deben sumar 1.0, respetando las proporciones relativas que cada elemento tiene en la lista original.
    Desarrollar también un programa que permita verificar el comportamiento de la función.
    Por ejemplo, normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].
"""
from typing import List

def normalizar_numeros(lista: [int]) -> List[int]:
    total = sum(lista)
    numeros = [x / total for x in lista]
    return numeros

def main()-> None:
    print(f"Lista Original: {lista}")
    print(f"Lista Normalizada: {normalizar_numeros(lista)}")
    
lista = [9, 16, 25, 36, 49, 64, 81, 100, 121, 144]

if __name__ == "__main__":
    main()
