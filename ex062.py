primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} > ".format(termo), end='')
        termo += razao
        cont += 1
    print("Pausa")
    mais = int(input("Quantos termos vocÊ quer mostrar a mais? "))
print("Progressão finalizada com {} termos mostrados.".format(total))