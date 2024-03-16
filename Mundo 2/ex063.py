n1 = 0
n2 = 1
c = 3
print("~"*21)
print("Calculo de fibonacci")
print("~"*21)
termo = int(input("Quantos termos você quer mostrar? "))
if termo > 2:
    print("{} - {}".format(n1,n2), end=" - ")
elif termo == 2:
    print("{} - {}".format(n1,n2), end=" - ")
elif termo == 1:
    print("{}".format(n1), end=" - ")
while c <= termo:
    n3 = n1 + n2
    print("{}".format(n3), end=' - ')
    n1 = n2
    n2 = n3
    c += 1
print("FIM")
print("=="*20)
