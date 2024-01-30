m = 0
me = 0
for c in range(1,6):
    p = float(input("Digite o peso da {}° pessoa: ".format(c)))
    if c == 1:
        m = p
        me = p
    if p > m:
        m = p
    if p < me:
        me = p
print("O maior peso foi {} e menor peso foi {}".format(m,me))
