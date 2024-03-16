from random import randint

def sorteia():
    numeros = []
    for c in range(0,5):
        numeros.append(randint(0,10))
    print(f"Sorteando 5 valores da lista: ", end="")
    for c in numeros:
        print(c,end=" ")
    print("PRONTO!")
    return numeros
def somaPar(numeros):
    pares = 0
    for c in numeros:
        if c % 2 == 0:
            pares += c
    print(f"Somando os valores pares de {numeros}, temos {pares}")

somaPar(sorteia())