

#Control de flujo
#Estructura Condicional
"""
En phyton podemos hacer distintas operaciones dependiendo de la opción que elijamos, esto lo podemos hacer con
la función if, la cual contiene el elif y el else.
Normalmente, if es para la primera condición y elif para las siguientes, else es para decir que si ninguna de
las opciones mostradas por los if son verdaderas el programa muestre la suya.

Este es un ejemplo creando una calculadora usando el condicional.
"""


#Pedimos opción y la almacenamos en una variable llamada operación.
operacion = float(input("Escoja una opción: \n1.Suma, \n2.Resta, \n3.Multiplicación, \n4.Division, \n5.Modulo\n"))

#Hacemos una condición con if para que haga distintas operaciones dependiendo de la opción.
if operacion == 1:
    num1 = float(input("Escribe el primer numero\n"))
    num2 = float(input("Escribe el segundo número\n"))
    #Transformamos el float en un string para poder concatenarlo
    print("El resultado es: " + str(num1 + num2))
elif operacion == 2:
    num1 = float(input("Escribe el primer numero\n"))
    num2 = float(input("Escribe el segundo número\n"))
    print("El resultado es: " + str(num1 - num2))
elif operacion == 3:
    num1 = float(input("Escribe el primer numero\n"))
    num2 = float(input("Escribe el segundo número\n"))
    print("El resultado es: " + str(num1 * num2))
elif operacion == 4:
    num1 = float(input("Escribe el primer numero\n"))
    num2 = float(input("Escribe el segundo número\n"))
    #Como no puedes dividir entre cero hacemos otro if para ver que hacer.
    if num2 == 0:
        print("No se puede dividir entre cero")
    else:
        print("El resultado es: " + str(num1 / num2))
elif operacion == 5:
    num1 = float(input("Escribe el primer numero\n"))
    num2 = float(input("Escribe el segundo número\n"))
    #Como no podemos hacer el módulo de 0 hacemos lo mismo que en la división.
    if num2 == 0:
        print("No se puede hacer el modulo de cero")
    else:
        print("El resultado es: " + str(num1 % num2))
elif operacion != (1,2,3,4,5):
    print("Opción no válida")