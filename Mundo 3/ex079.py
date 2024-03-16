# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista
# lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
while True:
    n = int(input("Digite um valor: "))
    if not lista.count(n):
        print("Valor adicionado com sucesso...")
        lista.append(n)
    else:
        print("Valor duplicado, Não será adicionado...")
    escolha = " "
    while escolha not in "SN":
        escolha = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if escolha in "N":
        break
print(f"Você digitou os valores {sorted(lista)}")
