print("-"*30)
print("{:^30}".format("MERCADINHO"))
print("-"*30)
menor = totpreco = totmil = baratoproduto = contador = 0
while True:
    produto = str(input("Nome do Produto: "))
    preco = float(input("Preço: R$"))
    contador += 1
    totpreco += preco
    if contador == 1 or preco < menor:
        menor = preco
        baratoproduto = produto
    if preco > 1000:
        totmil += 1
    pare = " "
    while pare not in "SN":
        pare = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if pare == "N":
        break
print("{:-^40}".format(" FIM DO PROGRAMA "))
print(f"O total da compra foi R${totpreco:.2f}")
print(f"Temos {totmil} produtos custando mais de R$1000,00")
print(f"O produto mais barato foi {baratoproduto} que custa R${menor:.2f}")
