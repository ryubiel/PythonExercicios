n = int(input("Digite um número: "))
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] convereter para HEXADECIMAL''')
opção = int(input("Sua opção: "))
if opção == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(n, bin(n)[2:]))
elif opção == 2:
    print("{} convertido para OCTAL é igual a {}".format(n, oct(n)[2:]))
elif opção == 3:
    print("{} convertido para HEXADECIMAL é igual a {}".format(n, hex(n)[2:]))
else:
    print("Opção invalida, tente novamente")