# Escribe un programa que intente dividir dos números. 
# Si el segundo número es cero, captura la excepción ZeroDivisionError. 
# Si el primer número es un número no válido, captura la excepción ValueError. 
# En cualquier caso, muestra un mensaje de error al usuario.
# Ejercicio 5

try:
    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))
    resultado = n1 / n2
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Error!No se puede dividir por cero")
except ValueError:
    print("Error!Debe ingresar números válidos")