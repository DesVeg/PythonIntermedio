#Imprimir un mensaje de error si no se pasan suficientes argumentos
def verificar_argumentos(*args):
    mensaje = "Argumentos suficientes" if len(args) >= 2 else "Error: no se pasaron suficientes argumentos"
    
    print(mensaje)

verificar_argumentos(10)