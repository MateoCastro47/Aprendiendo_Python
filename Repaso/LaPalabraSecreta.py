import random
print("---Bienvenido a la Palabra Secreta---")
palabras = ["Python", "Java", "Javascript", "Clase"]
palabraAleatoria = random.choice(palabras)
pistas = 3
intentos = 10
posicion = []
while intentos > 0:
    menu = "1.Jugar\n2.Pista\n3.Rendirse\n"
    opcion = float(input(menu))
    if opcion == 1:
        palabraUsuario = str(input("Escribe una palabra\n"))
        if palabraUsuario == palabraAleatoria:
            print("Has acertado")
        else:
            comunes = set(palabraUsuario) & set(palabraAleatoria)
            if comunes:
                print("Letras en común: " + str(comunes))
            else:
                print("No hay letras en común")
        intentos -= 1
    elif opcion == 2:
        opcion2 = float(input("¿Quieres una pista? \n 1.Si\n 2.No\n"))
        if opcion2 == 1:
            if pistas == 3:
                print("La palabra tiene " + str(len(palabraAleatoria)) + " caracteres")
                pistas -= 1
            elif pistas == 2:
                print(" La primera letra es: " + palabraAleatoria[0])
                pistas -= 1
            elif pistas == 1:
                print(" La última letra es: " + palabraAleatoria[-1])
                pistas -= 1
            else:
                print("No te quedan pistas")
    elif opcion == 3:
        print("Te has rendido")
        break
