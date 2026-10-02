#Escribe un programa que intente dividir dos números. Si el segundo número es cero, 
#captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.

n1 = 10
n2 = 0

try:
    resultado = n1 / n2
    print("Resultado:", resultado)

except ZeroDivisionError:
    print("Error!No se puede dividir por cero.")