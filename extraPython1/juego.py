import random
import os
hiadadhiohiawdiad

def dibujo(jugada):
    if jugada.capitalize() == "Piedra":
        print("                     @")
        print("                    @@@")
    if jugada.capitalize() == "Papel":
        print("                     =")
        print("                    ===")
    elif jugada.capitalize() == "Tijeras":
        print("                     |/")
        print("                     OO")


def grafico(score_hu, score_pc, turno):

    os.system("cls")

    print()
    print("          PIEDRA, PAPEL, TIJERAS: {} de 5".format(turno))
    print("         ---------------------------------------")
    print("          Jugador:  {} - {} : Ordenador".format(score_hu, score_pc))
    print("         ---------------------------------------")
    print()


def comprobar_ganador(jugador, ordenador):

    if jugador == "Piedra":
        if ordenador == "Piedra":
            gana = "Ninguno"
        elif ordenador == "Papel":
            gana = "Ordenador"
        else:
            gana = "Humano"

    elif jugador == "Papel":
        if ordenador == "Piedra":
            gana = "Humano"
        elif ordenador == "Papel":
            gana = "Ninguno"
        else:
            gana = "Ordenador"

    elif jugador == "Tijeras":
        if ordenador == "Piedra":
            gana = "Ordenador"
        elif ordenador == "Papel":
            gana = "Humano"
        else:
            gana = "Ninguno"

    return gana


def turno_jugador():

    opciones_humano = ["Piedra", "Papel", "Tijeras"]
    jugada = ""
    while jugada not in opciones_humano:
        jugada = input("              Haz tu jugada: ").capitalize()
    else:
        return jugada


def turno_ordenador(jugadas_humano, ultimo_resultado):

    if ultimo_resultado == 1:
        if jugadas_humano[-1] == "Piedra":
            jugada = random.choice(["Papel", "Piedra"])
        elif jugadas_humano[-1] == "Papel":
            jugada = random.choice(["Tijeras", "Papel"])
        elif jugadas_humano[-1] == "Tijeras":
            jugada = random.choice(["Piedra", "Tijeras"])
    elif ultimo_resultado == 0:
        if jugadas_humano[-1] == "Piedra":
            jugada = random.choice(["Tijeras", "Piedra"])
        elif jugadas_humano[-1] == "Papel":
            jugada = random.choice(["Piedra", "Papel"])
        elif jugadas_humano[-1] == "Tijeras":
            jugada = random.choice(["Piedra", "Tijeras"])

    return jugada


score_hu = 0
score_pc = 0
turno = 1
jugadas_humano = ["Piedra"]
ultimo_resultado = 1

while True:

    grafico(score_hu, score_pc, turno)

    jugada_humano = turno_jugador()

    jugada_ordenador = turno_ordenador(
        jugadas_humano, ultimo_resultado)

    gana = comprobar_ganador(jugada_humano, jugada_ordenador)

    print()
    dibujo(jugada_humano)
    print()
    dibujo(jugada_ordenador)
    print()
    print("             El ordenador: ", jugada_ordenador)
    print()

    jugadas_humano.append(jugada_humano)

    if gana == "Humano":
        turno += 1
        score_hu += 1
        ultimo_resultado = 1
        print("                     Ganaste.")
        print()
    elif gana == "Ordenador":
        turno += 1
        score_pc += 1
        ultimo_resultado = 0
        print("                Ganó el ordenador.")
    elif gana == "Ninguno":
        print("                     Empate.")
        print()

    input(" Pulsa cualquier tecla para continuar...")

    if turno == 6:
        grafico(score_hu, score_pc, 5)
        m1 = "FIN DE LA PARTIDA"
        if score_hu > score_pc:
            m2 = "  HAS GANADO"
        elif score_hu < score_pc:
            m2 = "  HAS PERDIDO"
        else:
            m2 = "       EMPATE"
        print()
        print()
        print("             {}".format(m1))
        print("             {}".format(m2))
        print()
        print()
        print()
        break
