v = int(input("Qual a velocidade do carro? "))
if v > 80:
    print("Você está acima do limite")
    print("Você foi multado em R${:.2f}".format((v-80) * 7))
else:
    print("Você está dentro do limite")