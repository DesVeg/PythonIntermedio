A={1, 2, 3, 4}
B={3, 4, 5, 6}

#1)Dados dos conjuntos, A y B, escribe un programa en Python que imprima los elementos que se encuentran en A o en B, o en ambos.
print(A | B)

#2)Dados dos conjuntos, A y B. escribe un programa en Python que imprima los elementos que se encuentran en A y en B
print(A & B)

#3)Dados dos conjuntos, A y B, escribe un programa en Python que imprima el conjunto de los elementos que se encuentran en A o en B, pero no en ambos.
print (A ^ B)

#4)Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto es un subconjunto de otro conjunto, B.
print(A.issubset(B))


#5)Dados un conjunto, A, escribe un programa en Python que imprima el número de elementos del conjunto.
print(len(A))