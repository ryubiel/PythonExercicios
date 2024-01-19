import random

e = int(input("Vamos jogar Jokenpô \nDigite 1 para escolher pedra\nDigite 2 para escolher papel\nDigite 3 para escolher tesoura\n: "))
maquina = random.randint(1,3)
print(maquina)
if e == 1:
    if maquina == 1:
        print("Empate")
    elif maquina == 2:
        print("Você ganhou")
    elif maquina == 3:
        print("Você perdeu")
elif e == 2:
    if maquina == 2:
        print("Empate")
    elif maquina == 1:
        print("Você ganhou")
    elif maquina == 3:
        print("Você perdeu")
elif e == 3:
    if maquina == 3:
        print("Empate")
    elif maquina == 2:
        print("Você ganhou")
    elif maquina == 1:
        print("Você perdeu")
