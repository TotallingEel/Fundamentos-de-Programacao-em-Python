def validador(mensagem):
    valido = 0
    while valido == 0:

        opcao = input(mensagem)

        if opcao == "":
            print("Inválido")
            continue

        valido = 1

        for i in range(len(opcao)):
            caractere = opcao[i]

            if not('0' <= caractere <= '9'):
                print("Tente Novamente")
                valido = 0
                break 
            
    return int(opcao)

def tabuada():

    while True:

        print("=== Bem Vindo a Tabuada ===")

        tabuadaNumero = int(input("Digite um número: "))

        print("\n")

        for i in range (0, 11):
            print(f"{tabuadaNumero} x {i} = {tabuadaNumero * i}")

        print("\n")

        escolha = validador("Digite 0 [Permanece] e 1 [Sair]: ")
                
        if escolha == 1:
            return 0

def game ():

    quantidade = 0
    soma = 0

    print("=== Em Jogo ===")

    while True:

        numero = int(input("Digite um número: "))

        if numero == 7:
            print("Você Acertou !!! \n")
            break

        quantidade += 1
        soma += numero

    return quantidade, soma

def estatistica(quantidade, soma):

    print("=== Resumo ===")

    print(f"Quantidade: {quantidade}")
    print(f"Soma: {soma}")
    print(f"Média: {soma}/{quantidade} = {soma/quantidade}")

def menu():

    operador = 1
    quantidade = 0
    soma = 0


    while operador != 0:

        print("=== Bem Vindo ao Jogo ===")

        print("1. Jogar")
        print("2. Tabuada")
        print("3. Estatistica")
        print("4. Sair")

        escolha = validador("Digite a opção: ")

        match escolha:
            case 1:
                quantidade, soma = game()
            case 2:
                tabuada()
            case 3:
                estatistica(quantidade, soma)
            case 4:
                print("Até Mais")
                operador = 0
            case _:
                print("Opção Inválida")

menu()