from time import sleep

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
e = False
while not e:
    print('[ 1 ] somar \n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    o = int(input(">>>>> Qual é a sua opção? "))
    if o == 5:
        e = True
    elif o == 1:
        print("A soma entre {} + {} é {}".format(n1,n2,n1+n2))
    elif o == 2:
        print("A multiplicação de {} X {} é {}".format(n1,n2,n1*n2))
    elif o == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("Entre {} e {} o maior valor é {}".format(n1, n2, maior))
    elif o == 4:
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
        print("Valores trocados")
    else:
        print("Número inválido, tente novamente")
    print("=-=" * 8)
    sleep(2)

print("Fim do programa")