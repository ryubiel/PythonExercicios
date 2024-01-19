from datetime import date
ano = int(input("Qual ano você nasceu? "))
anoAtual = date.today().year
idade = anoAtual - ano
if idade < 17:
    print("No futuro, você precisará se alistar")
    falta = 17 - idade
    print("Falta {} anos para você se alistar".format(falta))
elif idade == 17 or idade == 18:
    print("já está na hora de se alistar")
else:
    falta = idade - 18
    print("Você se alistou ou está atrasado de se alistar há {} anos".format(falta))