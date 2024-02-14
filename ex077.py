palavras = ("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON", "CURSO", "GRATIS", "ESTUDAR", "PRATICAR",
            "TRABALHAR", "MERCADO", "PROGRAMADOR", "FUTURO")
for pos in palavras:
    print(f"\nNa palavra {pos} temos ",end='')
    for vogais in pos:
        if vogais in "AEIOU":
            print(vogais,end=" ")