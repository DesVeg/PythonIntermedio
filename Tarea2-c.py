#Escribe un programa que intente acceder a una clave que no existe en un 
# diccionario. Si se produce una excepción KeyError, captura la excepción y muestra

persona = {
    "nombre": "Juan",
    "edad": 25
}

try:
    print(persona["apellido"])

except KeyError:
    print("Error!La clave no existe en el diccionario.")