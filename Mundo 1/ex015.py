d = int(input("Quantos dias alugados? "))
r = float(input("Quantos Km rodados? "))
t = (d*60) + (0.15*r)
print("O total a pagar é de R${:.2f}".format(t))