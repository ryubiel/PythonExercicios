def aumentar(preço = 0, taxa = 0):
    aumenta = preço + (preço * taxa / 100)
    return aumenta


def diminuir(preço = 0, taxa = 0):
    diminui = preço - (preço * taxa / 100)
    return diminui


def metade(preço = 0):
    metade = preço / 2
    return metade


def dobro(preço = 0):
    dobro = preço * 2
    return dobro


def moeda(preço = 0, moeda = "R$"):
    return f'{moeda}{preço:>.2f}'.replace(".",",")