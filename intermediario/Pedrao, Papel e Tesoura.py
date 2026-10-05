import random 

def validador(messagem):

    valido = 0
    while valido == 0:

        opcao = input(messagem)

        if opcao == "":
            print("Inválido")
            continue

        valido = 1

        for i in range(len(opcao)):
            caractere = opcao[i]

            if not('0' <= caractere <= '9'):
                print("Inválido, Tente Novamente")
                valido = 0
                break
    
    return int(opcao)

def game():

    jogadorVitoria = 0
    computadorVitoria = 0
    escolha = ["pedra", "papel", "tesoura"]

    print("Vamos Jogar Pedra, Papel ou Tesoura")

    while jogadorVitoria < 2 and computadorVitoria < 2:

        escolhaJogador = input("Esolha Pedra, Papel ou Tesoura: ").lower()

        escolhaComputador = random.choice(escolha)

        print(f"Escolha do Computador: {escolhaComputador}")

        if (escolhaJogador == "pedra" and escolhaComputador == "tesoura") or (escolhaJogador == "tesoura" and escolhaComputador == "papel") or (escolhaJogador == "papel" and escolhaComputador == "pedra"):
            vitoria = "Jogador"

        elif escolhaJogador == escolhaComputador:
            vitoria = "Empate"

        else:
            vitoria = "Computador"

        if vitoria == "Jogador":
            jogadorVitoria += 1

            print("Você Ganhou \n")

        elif vitoria == "Computador":
            computadorVitoria += 1

            print("Computador Ganhou \n")

        else:
            print("Empatados \n")

        print(f"Score - Jogador: {jogadorVitoria}, Computador: {computadorVitoria}")

    if jogadorVitoria > computadorVitoria:
        print("Parabéns, você ganhou")

    else:
        print("Computador Ganhou, tenha mais sorte na próxima vez")

def menu():

    operador = 1

    while operador != 0:

        print("=" * 3 + " Bem Vindo ao Sistema " + "=" * 3)

        print("1. Jogar \n2. Sair")

        escolha = validador("Digite a Opção: ")

        match escolha:
            case 1:
                game()
            case 2:
                print("Até Mais")
                operador = 0
            case _:
                print("Inválido")

menu()