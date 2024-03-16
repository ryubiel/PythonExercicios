#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.

lista = []
for c in range(0, 5):
    lista.append(int(input(f"Digite um valor para a posição {c}: ")))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print("=-" * 30)
print(f"Você digitou os valores {lista}")
print(f"O maior valor digitado foi {maior} nas posições ",end="")
for m,valor in enumerate(lista):
    if valor == maior:
        print(m, end="...")
print(f"\nO menor valor digitado foi {menor} nas posições ",end="")
for m,valor in enumerate(lista):
    if valor == menor:
        print(m, end="...")
