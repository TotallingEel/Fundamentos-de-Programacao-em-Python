operador = 1
novoValorRenda = 0 
soma = 0

listaGastos = []
listaValorGastos = []

while operador != 0:

    print("=============================================")

    print("Controle Financeiro")

    print("=============================================")

    print("1 - Informar Renda Mensal")
    print("2 - Cadastrar gasto")
    print("3 - Consultar gastos")
    print("4 - Consultar situação financeira")
    print("5 - Ver estatísticas")
    print("6 - Sair")

    print("=============================================")

    valido = 0
    while valido == 0: 

        entrada = input("Digite a opção: ")

        if entrada == "":
            print("Entrada Inválida")
            continue

        valido = 1

        for i in range(len(entrada)):
            caractere = entrada[i]
            if not('0' <= caractere <= '9'):
                print("Inválido, Tente Novamente \n")
                valido = 0
                break

    if valido == 1:
        escolha = int(entrada)
        
        match escolha:

            case 1:

                operadorRenda = 1

                while operadorRenda != 3:

                    print("=============================================")
                    print("=== Renda ===")
                    print("=============================================")

                    print("=============================================")
                    print("1. Informar Renda")
                    print("2. Consultar Renda")
                    print("3. Sair")
                    print("=============================================")

                    validoRenda = 0
                    while validoRenda == 0:

                        entradaRenda = input("Digite a opção: ")

                        if entradaRenda == "":
                            print("Entrada Inválida")
                            continue

                        validoRenda = 1

                        for j in range (len(entradaRenda)):
                            caractereRenda = entradaRenda[j]

                            if not('0' <= caractereRenda <= '9'):
                                print("Inválido, Tente Novamente \n")
                                validoRenda = 0
                                break

                    if validoRenda == 1:
                        escolhaRenda = int(entradaRenda)

                        match escolhaRenda:
                            case 1:
                                print("=== Informe a Renda ===")

                                while True:
                                    informeRenda = float(input("Digite a sua Renda: "))

                                    if informeRenda >= 0:
                                        novoValorRenda += informeRenda
                                        print("Renda Cadastrada")
                                        operadorRenda = 1
                                        break
                                    else:
                                        print("Renda Inválida, informe Novamente")

                            case 2:
                                print(f"A sua renda atual é {novoValorRenda:.2f}")

                                operadorRenda = 1
                            case 3:
                                print("Até Mais")

                                operadorRenda = 3
                            case _:
                                print("Opção Inválida")

            case 2:

                operadorGastos = 1
                
                while operadorGastos != 6: 
                    print("=============================================")
                    print("=== Cadastrar Gastos ===")
                    print("=============================================")
                
                    print("=============================================")
                    print("1. Alimentação")
                    print("2. Transporte")
                    print("3. Saúde")
                    print("4. Lazer")
                    print("5. Outros")
                    print("6. Sair")
                    print("=============================================")

                    validoGastos = 0
                    while validoGastos == 0:

                        entradaGastos = input("Digite a opção: ")

                        if entradaGastos == "":
                            print("Entrada Inválida")
                            continue

                        validoGastos = 1

                        for k in range(len(entradaGastos)):
                            caractereGastos = entradaGastos[k]

                            if not('0' <= caractereGastos <= '9'):
                                print("Inválido, Tente Novamente")
                                validoGastos = 0
                                break

                    if validoGastos == 1:
                        escolhaGastos = int(entradaGastos)

                        match escolhaGastos:

                            case 1:

                                print("== Alimentação ==")

                                listaGastos.append("Alimentação")

                                print("Alimentação Cadastrada")

                                while True:

                                    informeGastos = float(input("Digite o valor de seu gasto: "))

                                    if informeGastos >= 0:
                                        listaValorGastos.append(informeGastos)
                                        soma += informeGastos
                                        print("Valor Cadastrado")
                                        operadorGastos = 1
                                        break
                                    else:
                                        print("Valor Inválido, digite novamente")

                            case 2:

                                print("== Tranporte ==")
                                
                                listaGastos.append("Transporte")
                                
                                print("Transporte Cadastrada")
                                
                                while True:
                                
                                    informeGastos = float(input("Digite o valor de seu gasto: "))
                                
                                    if informeGastos >= 0:
                                        listaValorGastos.append(informeGastos)
                                        soma += informeGastos
                                        print("Valor Cadastrado")
                                        operadorGastos = 1
                                        break
                                    else:
                                        print("Valor Inválido, digite novamente")

                            case 3:
                                 
                                print("== Saúde ==")
                                                                
                                listaGastos.append("Saúde")
                                                                
                                print("Saúde Cadastrada")
                                                                
                                while True:
                                                                
                                    informeGastos = float(input("Digite o valor de seu gasto: "))
                                                                
                                    if informeGastos >= 0:
                                        listaValorGastos.append(informeGastos)
                                        soma += informeGastos
                                        print("Valor Cadastrado")
                                        operadorGastos = 1
                                        break
                                    else:
                                        print("Valor Inválido, digite novamente")
                            case 4:

                                print("== Lazer ==")
                                                                                                
                                listaGastos.append("Lazer")
                                                                                                
                                print("Lazer Cadastrada")
                                                                                                
                                while True:
                                                                                                
                                    informeGastos = float(input("Digite o valor de seu gasto: "))
                                                                                                
                                    if informeGastos >= 0:
                                        listaValorGastos.append(informeGastos)
                                        soma += informeGastos
                                        print("Valor Cadastrado")
                                        operadorGastos = 1
                                        break
                                    else:
                                        print("Valor Inválido, digite novamente")

                            case 5:
                                
                                print("== Outros ==")
                                                                                                
                                listaGastos.append("Outros")
                                                                                                
                                print("Outros Cadastrada")
                                                                                                
                                while True:
                                                                                                
                                    informeGastos = float(input("Digite o valor de seu gasto: "))
                                                                                                
                                    if informeGastos >= 0:
                                        listaValorGastos.append(informeGastos)
                                        soma += informeGastos
                                        print("Valor Cadastrado")
                                        operadorGastos = 1
                                        break
                                    else:
                                        print("Valor Inválido, digite novamente")

                            case 6:
                                print("Até Mais")
                                operadorGastos = 6
                            case _:
                                print("Opção Inválida, Digite Novamente")

            case 3:

                print("== Consultar Gastos ==")

                if len(listaGastos) == 0:
                    print("Sem gastos ou valor cadastrados")
                    operador = 1
                    continue
                else:
                    for l in range(len(listaValorGastos)):
                        print(f"{listaGastos[l]}: {listaValorGastos[l]}")

                    soma = 0
                    for s in listaValorGastos:
                        soma += s

                    print(f"O valor total de gastos cadastrados é: R$ {soma:.2f}")
                    operador = 1
                    continue

            case 4:
                
                print("== Consultar Situação Financeira ==")

                if soma > novoValorRenda:
                    print(f"Cuidado, seus gastos estão acima do valor de sua renda, você está com um déficit de R$ {soma - novoValorRenda:.2f}")
                    operador = 1
                elif soma == novoValorRenda:
                    print(f"Situação no limite: a soma dos seus gastos empata exatamente com sua renda (R$ {novoValorRenda:.2f})")
                    operador = 1
                else:
                    print(f"Está no caminho certo, sua situação apresenta um saldo positivo de R$ {novoValorRenda - soma:.2f}")
                    operador = 1

            case 5:
                print("========================================")
                print("     === Estatísticas === ")
                print("========================================")

                if (soma > 0):

                    print(" Percentual de Comprometimento: ")

                    for p in range(len(listaValorGastos)):
                        print(f"{listaGastos[p]}: {(listaValorGastos[p]/soma)*100:.2f}%")

                    operador = 1
                else:
                    print(" Não há gastos registados para gerar estatísticas. ")
                    operador = 1

                print("========================================")
                print("     === Gráfico === ")
                print("========================================")

                if len(listaGastos) > 0:

                    for r in range(len(listaGastos)):

                        print(f"{listaGastos[r]}: ", end = "")

                        barra = int(listaValorGastos[r]/10)

                        for a in range(barra):
                            print("█", end = "")
                        print("\n")
                    
                else:
                    print("Não podemos montar os Gráficos")
                    
            case 6:
                print("Até Mais")
                operador = 0
            case _:
                print("Opção Inválida")