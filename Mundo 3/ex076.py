lista = ("Caderno", 15.90,
         "Lápis", 1.75,
         "Borracha", 2,
         "Lapiseira", 2.99,
         "Estojo", 25,
         "Mochila", 150,
         "Caneta", 3,
         "Livro", 34.90)
print("-" * 40)
print(f"{'LISTA DE PREÇOS':^40}")
print("-" * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f"{lista[pos]:.<30}", end="")
    else:
        print(f"R${lista[pos]:>7.2f}")
print("-" * 40)