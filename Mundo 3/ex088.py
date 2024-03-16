#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e
# vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
total = 1
jogo = []
jogos = []
sorteios = int(input("Quantos jogos voce quer que eu sorteie? "))
print("-=" * 16)
while total <= sorteios:
    c = 0
    while True:
        numero = randint(1,60)
        if numero not in jogo:
            c += 1
            jogo.append(numero)
        if c >= 6:
            break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    total += 1
print(f"Sorteando seus {sorteios} jogos")
print("-=" * 16)
for i, l in enumerate(jogos):
    print(f"Jogo: {i+1}: {l}")
    sleep(1)
print("-=" * 5,"Boa sorte", "-=" * 5)
