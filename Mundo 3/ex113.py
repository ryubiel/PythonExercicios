def leiaInt(s):
    while True:
        try:
            n = int(input(s))
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[0;31mEntrada de dados interrompida pelo usuário.\033[m")
            return 0
        else:
            return n


def leiaFloat(s):
    while True:
        try:
            n = float(input(s))
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Digite um número real válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[0;31mEntrada de dados interrompida pelo usuário.\033[m")
            return 0
        else:
            return n


i = leiaInt("Digite um número inteiro: ")
r = leiaFloat("Digite um número real: ")
print(f"O valor inteiro digitado foi {i} e o real foi {r}")