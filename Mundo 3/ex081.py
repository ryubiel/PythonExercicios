#Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
while True:
    lista.append(int(input("Digite um valor: ")))
    escolha = " "
    while escolha not in "SN":
        escolha = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if escolha in "N":
        break
print("=-" * 20)
print(f"Você digitou {len(lista)} elementos")
lista.sort(reverse=True)
print(f"Você digitou os valores {lista}")
if 5 in lista:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não foi encontrado na lista!")
