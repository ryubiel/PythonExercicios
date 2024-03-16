def aumentar(preço, taxa):
    aumenta = preço + (preço * taxa / 100)
    return aumenta

def diminuir(preço, taxa):
    diminui = preço - (preço * taxa / 100)
    return diminui

def metade(preço):
    metade = preço / 2
    return metade

def dobro(preço):
    dobro = preço * 2
    return dobro