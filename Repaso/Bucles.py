#Bucles
"""
En python existen bucles como en Java, pero solo comparten dos, While y for.
1. El bucle While nos permite realizar una línea de código las veces que queramos hasta que la
condición que le propongamos sea falsa, por ejemplo:
"""

#Inicializamos la variable que vamos a usar.
a = 1
#Expresamos la condición
while a < 10:
    print("Soy un bucle while")
    #Aumentamos la variable a para que el bucle no sea infinito.
    a = a + 1
print("")
for i in range (1,10):
    print("Soy un bucle for")
print("")
palabra = "Python"
for i in palabra:
    print(i)
print("")
numeros = [2,3,4,1,24,89,5]
for i in numeros:
    print(i)
print("")
