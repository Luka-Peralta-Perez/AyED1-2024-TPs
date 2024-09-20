"""
    1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:
    
    a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos.

    b. Calcular y devolver el producto de todos los elementos de la lista anterior.

    c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar
    se ingresa desde el teclado y la función lo recibe como parámetro. No utilizar
    listas auxiliares.
    
    d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
    auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50]
"""
from random import randint

def lista_a():
    
    numero_random = [randint(1000, 9999) for _ in range(randint(10, 99))]
    return numero_random

def lista_b(lista):
    producto = 1
    for numero in lista:
        producto *= numero
    return producto

def lista_c(lista, valor):
    while valor in lista:
        lista.remove(valor)
    return lista

def es_capicua(lista):
    return lista == lista[::-1]

def main():
    lista_original = lista_a()
    print(f"Lista cargada {lista_original}\n")
    
    producto = lista_b(lista_original)
    print(f"el Producto de todos los elementos de la lista es de: {producto}\n")
    
    eliminar_valor = int(input("Ingrese el valor que desea eliminar: "))
    lista_actualizada = lista_c(lista_original, eliminar_valor)
    print(f"\nResultado de la lista con los valores ingresados eliminados {lista_actualizada}")
    
    print(f"La lista {lista_actualizada}, es capicua? {es_capicua(lista_actualizada)}")
    
if __name__ == "__main__":
    main()
    
    
    

