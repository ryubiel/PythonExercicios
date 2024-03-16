def leiaInt(s):
    while True:
        n = str(input(s))
        if n.isnumeric():
            n = int(n)
            return n
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")