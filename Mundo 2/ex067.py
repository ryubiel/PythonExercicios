while True:
    print("-"* 30)
    n = int(input("Quer ver a tabuada de qual valor? "))
    print("-" * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print("{} x {} = {}".format(n, c, c * n))
print("PROGRAMA TABUADA ENCERRADO. volte sempre!")