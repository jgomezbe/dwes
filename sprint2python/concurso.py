i = 0
score = 0

print(" El mejor jugador de fútbol de la historia es: ")
print(" Lionel Messi (a)")
print(" Diego Armando Maradona (b)")
print(" Cristiano Ronaldo (c) ")
op = input('Elige: ')
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
else:
    print(" La opción tecleada es inválida.")

print(" El mejor tenista de la historia es: ")
print(" Novak Djokovic (a)")
print(" Rafa Nadal (b)")
print(" Roger Federer (c) ")
op = input('Elige: ')
if op == "a":
    print(' Has fallado :( .\n')
    score -= 5
    i += 1
elif op == "b":
    print(' Has acertado :) .')
    score += 10
    i = 3
elif op == "c":
    print(' Has fallado :( .\n')
    score -= 5
    i += 1
else:
    print(" La opción tecleada es inválida.")

print(" El mejor jugador de ba de la historia es: ")
print(" Michael Jordan (a)")
print(" LeBron James (b)")
print(" Magic Johnson (c) ")
op = input('Elige: ')
if op == "a":
    print(' Has acertado :) .')
    score += 10
    i = 3
elif op == "b":
    print(' Has fallado :( .\n')
    score -= 5
    i += 1
elif op == "c":
    print(' Has fallado :( .\n')
    score -= 5
    i += 1
else:
    print(" La opción tecleada es inválida.")

print(" \nHas obtenido "+str(score)+" puntos en "+str(i)+" intentos.")
