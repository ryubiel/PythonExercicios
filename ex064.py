soma = total = d = 0
while d != 999:
    d = int(input("Digite um número [999 para parar]: "))
    if d != 999:
        soma += d
        total += 1
print("Você digitou {} números e a soma entre eles foi {}.".format(total,soma))
