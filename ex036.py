v = float(input("Qual o valor da casa a ser comprada? R$"))
s = float(input("Qual o seu salário por mês? R$"))
a = int(input("Em quantos anos você quer pagar a casa? "))
f = s * 30/100
tm = a * 12
pm = v / tm
if pm > s:
    print("O valor da casa é maior que o seu salário, não é possível aprovar o empréstimo")
elif pm > f:
    print("O valor excede 30% do seu salário, não é possível aprovar o empréstimo")
else:
    print("Empréstimo aprovado!!!")