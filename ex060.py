numero = int(input("Digite um número para calcular seu Fatorial: "))
f = 1
cont = numero
while cont > 0:
    print("{}".format(cont), end="")
    print(" x " if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1
print('{}'.format(f))
