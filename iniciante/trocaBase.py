print("="*5 + " Calculadora de Mudança de Base " + 5*"=")
operador = 1

while operador != 0:

    print("1. Binário")
    print("2. Octal")
    print("3. Hexadecimal")
    print("4. Sair")

    valido = 0
    while valido == 0:
        
        opcao = input("Digite a opção: ")

        if opcao == "":
            print("Inválido, tente novamente")
            continue

        valido = 1

        for i in range(len(opcao)):
            caractere = opcao[i]

            if not('0' <= caractere <= '9'):
                print("Inválido, tente novamente")
                valido = 0
                break

    if valido == 1:
        escolha = int(opcao)
        match escolha:
            case 1:
                print("="*3 + "Binário" + 3*"=")

                numero = int(input("Digite um número decimal: "))
                binario = []

                if numero == 0:
                    binario.append(0)
                else:
                    while numero != 0:
                        modulo = numero % 2
                        binario.append(modulo)
                        numero = numero // 2

                binario.reverse()

                binario_string = ""
                for i in binario:
                    binario_string += str(i)
                print(f"Equivalente em Binário: {binario_string}")
                print()
                operador = 1
                
            case 2:
                print("="*3 + "Octal" + 3*"=")

                number = int(input("Digite um número decimal: "))
                octal = []

                if number == 0:
                    octal.append(0)
                else:
                    while number != 0:
                        resto = number % 8
                        octal.append(resto)
                        number = number // 8

                octal.reverse()

                octal_string = ""
                for j in octal:
                    octal_string += str(j)
                print(f"Equivalente em octal: {octal_string}")
                print()
                operador = 1

            case 3:
                print("="*3 + "Hexadecimal" + 3*"=")

                hexaLetra = ['A', 'B', 'C', 'D', 'E', 'F']
                nombre = int(input("Digite um número em decimal: "))
                hexa = []

                if nombre == 0:
                    hexa.append(0)
                else:
                    while nombre != 0:
                        r = nombre % 16
                        if r > 9:
                            i = 10
                            for letra in hexaLetra:
                                if i == r:
                                    hexa.append(letra)
                                    break
                                i += 1
                        else:
                            hexa.append(r)
                        nombre = nombre // 16
                hexa.reverse()

                hexa_string = ""
                for k in hexa:
                    hexa_string += str(k)
                print(f"Equivalente em hexadecimal: {hexa_string}")
                print()
                operador = 1

            case 4:
                print("Até Mais")
                operador = 0
            case _:
                print("Inválido, opção inexistente")