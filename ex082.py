#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os
# valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = []
par = []
impar = []
while True:
    lista.append(int(input("Digite um valor: ")))
    escolha = " "
    while escolha not in "SN":
        escolha = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if escolha in "N":
        break
for c, n in enumerate(lista):
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f"A lista completa é {lista}")
print(f"A lista de pares é {par}")
print(f"A lista de impares é {impar}")
