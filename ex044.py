p = float(input("Preço das compras: R$"))
c = int(input('''FORMAS DE PAGAMENTO
[ 1 ] = à vista dinheiro/cheque
[ 2 ] = à vista no cartão 
[ 3 ] = em até 2x no cartão 
[ 4 ] = 3x ou mais no cartão
Qual é a opção: '''))
if c == 1:
    v = (p * 10) / 100
    print("O valor a ser pago é {}".format(p - v))
elif c == 2:
    v = (p * 5) / 100
    print("O valor a ser pago é {}".format(p - v))
elif c == 3:
    print("O valor a ser pago é {}".format(p))
elif c == 4:
    v = (p * 20) / 100
    print("O valor a ser pago é {}".format(p + v))
else:
    print("opção invalida")