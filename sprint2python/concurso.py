
cont = 3
i = 0
score = 0
while i < 3:
    print(" El mejor jugador de fútbol de la historia es: ")
    print(" Lionel Messi (a)")
    print(" Diego Armando Maradona (b)")
    print(" Cristiano Ronaldo (c) ")
    op = input('Elige sabiamente: ')

    if op == "a":
        print(' Has fallado :( .\n')
        score -= 5
        i += 1
    elif op == "b":
        print(' Has fallado :( .\n')
        score -= 5
        i += 1
    elif op == "c":
        print(' Has acertado :) .')
        score += 10
        i = 3
        print
    else:
        print(" La opción tecleada es inválida.")
print(" \nHas obtenido "+str(score)+" puntos en "+str(i)+" intentos.")
