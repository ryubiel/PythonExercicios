continua = "S"
contador = soma = 0
while continua == 'S':
    n = int(input("Digite um número: "))
    if contador == 0:
        maior = menor = n
    contador += 1
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    continua = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
print("Você digitou {} números e a média foi {}".format(contador, soma/contador))
print("O maior valor foi {} e o menor foi {}".format(maior,menor))
