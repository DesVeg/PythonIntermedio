#Escribe un programa que intente sumar un número y una cadena. Si se produce un error 
# de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.

num = 10
an = "Hola"

try:
    resultado = num + an
    print(resultado)

except TypeError:
    print("Error!No se puede sumar un número con una cadena.")