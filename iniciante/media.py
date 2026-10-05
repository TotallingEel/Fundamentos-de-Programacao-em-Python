
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))

if (0 <= n1 <= 10) and (0 <= n2 <= 10) and (0 <= n3 <= 10):
    media = (n1 + n2 + n3)/3
    print(f"Sua média: {media:.2f}")

    if media >= 7:
        print("Aprovado")
    elif media >= 4:
        print("Em Reposição")
        n4 = float(input("Digite a nota 4: "))
        mediaR = (media + n4)/2
        if mediaR >= 6:
            print("Segunda média: {mediaR:.2f}")
            print("Aprovado pela Reposição")
        else:
            print("Reprovado Pela Reposição")
    else:
        print("Reprovado por Nota")
else:
    print("Notas Inválidas")