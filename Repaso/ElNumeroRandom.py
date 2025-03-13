import random
intentos = 10
numeroAleatorio = float(random.randrange(1, 101))

while intentos > 0:

    numeroUsuario = float(input("Te quedan: " + str(intentos) + " intentos, escribe un número\n"))

    if numeroUsuario > numeroAleatorio:
        print("El número es menor")

    elif numeroUsuario < numeroAleatorio:
        print("El numero es mayor")

    else:
        print("Has acertado")
        print("Lo as hecho en: " + str(intentos) + " intentos")
        break

    intentos-= 1

if intentos == 0:
    print("Has perdido")
    print("El número era: " + str(numeroAleatorio))


