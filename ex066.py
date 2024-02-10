soma = total = 0
while True:
    d = int(input("Digite um número [999 para parar]: "))
    if d == 999:
        break
    soma += d
    total += 1
print(f"Você digitou {total} números e a soma entre eles foi {soma}.")
