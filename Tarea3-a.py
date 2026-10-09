#Calcular el mayor de dos números ingresados por teclado usando un operador ternario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

mayor = num1 if num1 > num2 else num2

print("El número mayor es:", mayor)