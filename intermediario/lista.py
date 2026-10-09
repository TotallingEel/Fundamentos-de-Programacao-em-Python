def validador(mensagem):

    valido = 0
    while valido == 0:

        escolha = input(mensagem)

        if escolha == "":
            print("inválido, nenhum caractere inserido")
            continue

        valido = 1

        for i in range(len(escolha)):
            caractere = escolha[i]

            if not('0' <= caractere <= '9'):
                print("Inválido, tente novamente")
                valido = 0
                break

    return int(escolha)

def sistema():

    operador = 1
    minhaLista = []

    while operador != 0:

        print("="*5 + " Sistema de Listas " + "="*5)

        print()

        if not minhaLista:
            print("Lista Vazia")
        else:
            indice = 0
            for elemento in minhaLista:
                print(f"{indice}. {elemento}")
                indice += 1

        print()

        print("-" * 15)
        print("1. Adicionar")
        print("2 Remover")
        print("3. Sair")
        print("-" * 15)

        opcao = validador("Digite a opção: ")

        print()

        match opcao:
            case 1:

                subOperador = 1
                while subOperador != 0:

                    print("="*3 + " Adicionar " + "="*3)

                    minhaEscolha = input("Digite um elemento de sua escolha: ")

                    minhaLista.append(minhaEscolha)

                    print("Sua escolha foi adicionada a lista")

                    print()

                    subOpcao = validador("Digite 1 [permancer] ou 0 [voltar]: ")

                    if subOpcao == 0:
                        subOperador = 0
            
            case 2:
                print("="*3 + " Remover " + "="*3)

                if not minhaLista:
                    print("Lista Vazia, não há o que remover")
                    continue

                subOpcaoRemover = validador("Digite 1 [remover] ou 0 [voltar]: ")

                if subOpcaoRemover == 1:
                    removido = minhaLista.pop()
                    print(f"O elemento {removido} foi removido da sua lista")
                else:
                    operador = 1

            case 3:
                print("Até Mais")
                operador = 0

            case _:
                print("Opção Inválida, sem vontade de novas funções ao sistema")

sistema()