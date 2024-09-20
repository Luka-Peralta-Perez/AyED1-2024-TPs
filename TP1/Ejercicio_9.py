"""
    9. Resolver el siguiente problema utilizando funciones:
    Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso
    para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y
    cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón
    caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso
    de alguna naranja se encuentra fuera del rango indicado se la clasifica para
    procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas
    cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para
    jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente
    reparto. Simular el peso de cada unidad generando un número entero al azar entre
    150 y 350.
    
    Además, se desea saber cuántos camiones se necesitan para transportar la cosecha, considerando
    que la ocupación del camión no debe ser inferior al 80%;
    en caso contrario el camión no serán despachado por su alto costo.

"""
from typing import List, Tuple
from random import randint

def cajones(l: List[int]) -> Tuple[int, int, int]:
    cajones_llenos = 0
    naranjas_jugo = 0
    sobrante = 0
    cajon_actual = []
    for n in l:
        if n >= 200 and n <= 300:
            cajon_actual.append(n)
            if len(cajon_actual) == 100:
                cajones_llenos += 1
                cajon_actual = []
        else:
            naranjas_jugo += 1
    if cajon_actual:
        sobrante = len(cajon_actual)
    return cajones_llenos, naranjas_jugo, sobrante

def camion_carga(camiones: int, cajones: List[int]) -> Tuple[int, int]:
    cajones_cargados = []
    peso = 0
    for cajon in cajones:
        peso += cajon
        if peso > camiones * 500_000:
            cajones_cargados.append((peso - cajon) / 1_000)
            peso = cajon
    return cajones_cargados, peso

def main():
    naranjas = int(input("Ingrese la cantidad de naranjas cosechadas: "))
    pesos = [randint(150, 350) for _ in range(naranjas)]  # assuming a random weight between 150 and 350g per orange
    cajones_llenos, naranjas_jugo, sobrante = cajones(pesos)
    print(f"Se pueden llenar {cajones_llenos} cajones.")
    print(f"{naranjas_jugo} naranjas para jugo.")
    print(f"Se tiene un sobrante de {sobrante} naranjas.")

    cajones_pesos = []
    cantidad = 0
    peso = 0
    for naranja in pesos:
        if naranja >= 200 and naranja <= 300:
            peso += naranja
            cantidad += 1
        if cantidad == 100:
            cajones_pesos.append(peso)
            cantidad = 0
            peso = 0
    if cantidad:
        cajones_pesos.append(peso)

    camiones_cargados, ultimo = camion_carga(20, cajones_pesos)
    for i, peso in enumerate(camiones_cargados):
        if i < 20:
            print(f'En el camión {i + 1:>2} van {peso} kilos.')

    if len(camiones_cargados) > 20:
        print(f'\nHay carga para despachar {len(camiones_cargados) - 20} camiones más.')
    else:
        print(f'\nHay carga para despachar {len(camiones_cargados)} camiones completos.')
    if (ultimo / 1_000) < (500_000 * 0.80):
        print(f'Y no hay suficiente carga para despachar el último camión\nsolo hay {ultimo} para el último camión.')
if __name__ == "__main__":
    main()