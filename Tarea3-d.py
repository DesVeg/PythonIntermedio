#Calcular el promedio de una lista de números usando args y un operador ternario
def calcular_promedio(*args):
    promedio = sum(args) / len(args) if len(args) > 0 else 0

    print("Promedio:", promedio)


numeros = input("Ingrese números separados por espacios: ").split()

numeros = [float(numero) for numero in numeros]

calcular_promedio(*numeros)