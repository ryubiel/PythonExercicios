#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep


def contador(a, b, c):
    if c == 0:
        print("Impossível realizar contagem com passo zerado, alterando valor de passo para 1")
        c = 1
    print("=-" * 30)
    print(f"Contagem de {a} até {b} de {c} em {c}")
    sleep(1.5)
    for cont in range(a, b + 1, c):
        print(f"{cont}", end=" ")
        sleep(0.5)
    print("FIM!")


contador(1, 10, 1)
contador(10, 0, -2)
print("Agora é sua vez de personalizar a contagem!")
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i,f,p)
