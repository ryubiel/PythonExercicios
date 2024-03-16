def ficha(j="<desconhecido>", g=0):
    print(f"O jogador {j} fez {g} gol(s) no campeonato.")


jogador = str(input("Nome do Jogador: "))
gol = str(input("Número de Gols: "))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jogador.strip() == "":
    ficha(g=gol)
else:
    ficha(jogador,gol)
