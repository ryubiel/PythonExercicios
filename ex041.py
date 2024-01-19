from datetime import date
ano = int(input("Qual ano de nascimento do atleta? "))
anoAtual = date.today().year
idade = anoAtual - ano
print(idade)
if idade <= 9:
    print("Atleta Mirim")
elif idade <= 14:
    print("Atleta Infantil")
elif idade <= 19:
    print("Atleta Junior")
elif idade == 20:
    print("Atleta Sênior")
else:
    print("Atleta Master")