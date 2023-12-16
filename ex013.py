s = float(input("Qual é o salário do funcionário? R$"))
n = s + (s * 15/100)
print("Um funcionário que ganhava R${},com 15% de aumento, passa a receber R${:.2f}".format(s,n))