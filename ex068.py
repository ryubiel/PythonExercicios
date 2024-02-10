from random import randint

total = 0
print("=-" * 15)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-" * 15)
while True:
    valor = int(input("Diga um valor: "))
    escolha = str(input("Par o Ìmpar [P/I] ")).upper().strip()[0]
    print("-" * 25)
    while escolha not in "PI":
        escolha = str(input("Par o Ìmpar [P/I] ")).upper().strip()[0]
    maqvalor = randint(0, 10)
    somavalores = valor + maqvalor
    if somavalores % 2 == 0:
        print(f"Você jogou {valor} e o computador {maqvalor}. Total de {somavalores} DEU PAR")
        print("-" * 25)
        if escolha in "P":
            print("Você VENCEU!")
        else:
            print("Você PERDEU!")
            break
    else:
        print(f"Você jogou {valor} e o computador {maqvalor}. Total de {somavalores} DEU ÍMPAR")
        print("-" * 25)
        if escolha in "I":
            print("Você VENCEU!")
        else:
            print("Você PERDEU!")
            break
    print("Vamos jogar novamente...")
    print("-" * 25)
    total += 1
print("=-" * 15)
print(f"GAME OVER! Você venceu {total} vezes.")
