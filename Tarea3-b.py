#Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario
def buscar_palabra(palabra, *args):
    resultado = "La palabra se encuentra en la lista" if palabra in args else "La palabra no se encuentra en la lista"

    print(resultado)


palabras = input("Ingrese palabras separadas por espacios: ").split()

buscar = input("Ingrese la palabra que desea buscar: ")

buscar_palabra(buscar, *palabras)