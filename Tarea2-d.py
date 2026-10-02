#Escribe un programa que intente abrir un archivo que no existe. 
# Si se produce una excepción FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. 
# Sin embargo, también intenta crear el archivo si no existe.
# Ejercicio 4

nombre_archivo = "archivo.txt"

try:
    archivo = open(nombre_archivo, "r")
    print(archivo.read())
    archivo.close()
except FileNotFoundError:
    print("Error: el archivo no existe.")
    print("Creando archivo...")
    archivo = open(nombre_archivo, "w")
    archivo.write("Archivo creado correctamente.")
    archivo.close()
    print("Archivo creado.")