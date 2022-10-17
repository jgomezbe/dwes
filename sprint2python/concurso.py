import random
def preguntas(i):
    score = 0
    if i == 1:
        print(" El mejor jugador de fútbol de la historia es: ")
        print(" Lionel Messi (a)")
        print(" Diego Armando Maradona (b)")
        print(" Cristiano Ronaldo (c) ")
        op = input('Elige: \n')
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
    elif i == 2:
        print(" El mejor tenista de la historia es: ")
        print(" Novak Djokovic (a)")
        print(" Rafa Nadal (b)")
        print(" Roger Federer (c) ")
        op = input('Elige: \n')
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

    elif i==3:
        print(" El mejor jugador de la NBA de la historia es: ")
        print(" Michael Jordan (a)")
        print(" LeBron James (b)")
        print(" Magic Johnson (c) ")
        op = input('Elige: \n')
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
    
    return score    

num1=random.randint(1,3)
score1=preguntas(num1)
num2=random.randint(1,3)
while num1==num2:
    num2=random.randint(1,3)
score2=preguntas(num2)
print(" \nHas obtenido "+str(score1+score2)+" puntos.")
