notas = []
medias = []
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    medias.append([nome, [nota1, nota2], media])
    notas.clear()
    escolha = " "
    while escolha not in "SN":
        escolha = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if escolha in "N":
        break
print("-" * 30)
print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':>8}")
print("-" * 26)
for i, a in enumerate(medias):
    print(f"{i:<5} {a[0]:<10}{a[2]:>8.1f}")
while True:
    print("=" * 30)
    opc = int(input("Mostrar notas de qual aluno? (Digite 999 para interromper) "))
    print("=" * 30)
    if opc == 999:
        print("FINALIZANDO...")
        break
    if opc <= len(medias) -1:
        print(f"Notas de {medias[opc][0]} são {medias[opc][1]}")
print("<<< VOLTE SEMPRE >>>")