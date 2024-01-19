n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2
print("Nota {}".format(m))
if m <= 5:
    print("Aluno reprovado")
elif 5 <= m <= 6.9:
    print("Aluno em recuperação")
else:
    print("Aluno aprovado")