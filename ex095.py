#Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
time = []
gols = []
jogador = {}
while True:
    jogador.clear()
    jogador = {'nome': str(input("Nome do jogador: "))}
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    gols.clear()
    for g in range(0,partidas):
        gols.append(int(input(f"   Quantos gols na partida {g + 1}? ")))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        escolha = str(input("Quer continuar? [S/N] ")).upper()[0]
        if escolha in "SN":
            break
        print("Erro! Por favor, digite apenas S ou N")
    if escolha == "N":
        break
print("-" * 40)
print("cod", end=' ')
for i in jogador.keys():
    print(f"{i:<15}", end='')
print()
print("-" * 40)
for k, v in enumerate(time):
    print(f"{k:>3}", end=' ')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print("-" * 40)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"ERRO! não existe jogador com código {busca}")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:")
        for i, g in enumerate(time[busca]['gols']):
            print(f"    No jogo {i+1} fez {g} gols.")
    print("-" * 40)
print(">>> VOLTE SEMPRE <<<")
