from datetime import date
maiores = 0
menores = 0
anoAtual = date.today().year
for c in range(1,8):
    ano = int(input("Digite o ano de nascimento da {}° pessoa: ".format(c)))
    idade = anoAtual - ano
    if idade > 18:
        maiores += 1
    else:
        menores += 1
print("{} pessoas não atigiram a maioridade e {} atingiram a maioridade".format(menores, maiores))