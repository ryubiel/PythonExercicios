somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for c in range(1,5):
    print("----- {}° Pessoa -----".format(c))
    n = str(input("Digite o nome: ")).strip()
    i = int(input("Digite a idade: "))
    s = str(input("Digite o sexo: [M/F]")).strip()
    somaidade += i
    if c == 1 and s in 'Mm':
        maioridadehomem = i
        nomevelho = n
    if s in "Mm" and i > maioridadehomem:
        maioridadehomem = i
        nomevelho = n
    if s in "Ff" and i < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print("A média de idade do grupo é de {} anos".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}".format(maioridadehomem,nomevelho))
print("Ao todo são {}^mulheres com menos de 20 anos".format(totmulher20))