maioridade = mulhermenor = homem = 0
while True:
    print("-" * 20)
    print("CADASTRE UMA PESSOA")
    print("-" * 20)
    i = int(input("Idade: "))
    s = " "
    while s not in "MF":
        s = str(input("Sexo: [M/F] ")).upper().strip()[0]
    print("-" * 20)
    if s == "M":
        homem += 1
    if i >= 18:
        maioridade += 1
    if i < 20 and s == "F":
        mulhermenor += 1
    escolha = " "
    while escolha not in "SN":
        escolha = str(input("Quer continuar [S/N] ")).upper().strip()[0]
    if escolha in "N":
        break
print(f"Total de pessoas com mais de 18 anos: {maioridade}")
print(f"Ao todo temos {homem} homens cadastrados")
print(f"E temos {mulhermenor} mulheres com menos de 20 anos")
