"""
    8. La siguiente función permite averiguar el día de la semana para una fecha determinada.
    La fecha se suministra en forma de tres parámetros enteros y la función devuelve 0 para domingo, 1 para lunes, 2 para martes, etc.
    Escribir un programa para imprimir por pantalla el calendario de un mes completo, correspondiente a un mes
    y año cualquiera basándose en la función suministrada. Considerar que la semana
    comienza en domingo.
    
def diadelasemana(dia,mes,año):
     if mes < 3:
        mes = mes + 10
        año = año – 1
        
     else:
        mes = mes – 2
        siglo = año // 100
        año2 = año % 100
        diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
        if diasem < 0:
        diasem = diasem + 7
      return diasem

"""
def dia_de_semana(dia: int, mes: int, anio: int):
    if mes < 3:
        mes = mes + 10
        anio = anio - 1
        diasem = dia  # Define diasem en este caso
    else:
        mes = mes - 2
        siglo = anio // 100
        año2 = anio % 100
        diasem = (((26*mes-2)//10) + dia + año2 + (año2//4) + (siglo//4) - (2*siglo)) %7
        
        if diasem < 0:
            diasem = diasem + 7
    return diasem
    

def bisiesto(anio):
    """  
    Un año es bisiesto si es divisible por 4, excepto si es divisible por 100,
    a menos que también sea divisible por 400.

    Pre:
    - 'anio' es un entero positivo.

    Post:
    - Devuelve 'True' si el año es bisiesto, de lo contrario, 'False'.
    
    """
    return anio % 4 == 0 and (anio % 100 !=0 or anio % 400 == 0)

def validar_fecha(dia: int, mes: int, anio: int) -> bool:
    """
    Verifica si una fecha es válida.

    Pre:
        dia (int): día de la fecha
        mes (int): mes de la fecha
        anio (int): año de la fecha

    Post:
           
    """
    mes_dias = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}
    if mes < 1 or mes > 12:
        return False
    if anio < 1:
        return False
    if mes == 2 and bisiesto(anio):
        return dia >= 1 and dia <= 29
    return dia >= 1 and dia <= mes_dias[mes]



def imprimir_calendario(mes: int, anio: int) -> None:
    """
    Imprime el calendario de un mes completo.

    Pre:
        mes (int): mes del calendario (1-12)
        anio (int): año del calendario

    Post:
        Imprime el calendario del mes y año especificados
    """
    dias_de_la_semana = {
        0: "Domingo",
        1: "Lunes",
        2: "Martes",
        3: "Miercoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sabado"
    }

    
    primer_dia_mes = dia_de_semana(1, mes, anio)

    # Imprimir los días de la semana
    print("  ".join(dias_de_la_semana.values()))

    # Imprimir el calendario
    dias_del_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes == 2 and bisiesto(anio):
        dias_del_mes[1] = 29

    for i in range(primer_dia_mes):
        print("   ", end=" ")
    for dia in range(1, dias_del_mes[mes-1]+1):
        print(f"{dia:3d}", end=" ")
        if (dia + primer_dia_mes) % 7 == 0:
            print()
    print()
    
def main()-> None:
    try:
        mes = int(input("Ingrese el mes (1-12): "))
        anio = int(input("Ingrese el año: "))

        if not validar_fecha(1, mes, anio):
            print("Fecha inválida")
        else:
            imprimir_calendario(mes, anio)
    except ValueError:
        print("ERROR: Los numeros ingresados deben ser correspondientes a los meses del año.")

if __name__ == "__main__":
    main()


