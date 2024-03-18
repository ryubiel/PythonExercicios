p = float(input("Digite o preço do produto: R$"))
d = int(input("Digite a porcentagem do desconto: "))
f = p*d/100
print("O produto no valor de R${:.2f}, com o desconto de {}%, fica R${:.2f}".format(p,d,p-f))