from random import randint

print("-=-" * 20)
print("Vou pensar em um número entre 0 e 10. Tente adivinhar...")
print("-=-" * 20)
r = randint(0 ,10)
j = int(input("Qual número eu pensei? "))
total = 0
while j != r:
    total += 1
    if j > r:
        print("Menos... tente mais uma vez")
    else:
        print("Mais... tente mais uma vez")
    j = int(input("Qual o seu palpite agora? "))
print("Você acertou com {} tentativas".format(total))
