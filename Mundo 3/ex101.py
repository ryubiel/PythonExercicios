def voto(ano):
    from datetime import date
    data = date.today().year
    idade = data - ano
    print(f"Com {idade} anos:", end=" ")
    if idade < 16:
        print("NÃO VOTA")
    elif idade >= 18:
        print("VOTO OBRIGATÓRIO")
    else:
        print("VOTO OPCIONAL")


nascimento = int(input("Em que ano você nasceu? "))
voto(nascimento)
