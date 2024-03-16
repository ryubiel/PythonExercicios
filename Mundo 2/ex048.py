s = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s += c
print("A soma os números ímpares múltiplos de três é {}".format(s))
