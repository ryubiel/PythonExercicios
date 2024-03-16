cinquenta = vinte = dez = um = 0
saque = int(input("Que valor você quer sacar? R$"))
while saque > 0:
    if saque >= 50:
        cinquenta += 1
        saque -= 50
    if saque >= 20:
        vinte += 1
        saque -= 20
    if saque >= 10:
        dez += 1
        saque -= 10
    if saque >= 1:
        um += 1
        saque -= 1
print(f"Total de {cinquenta} cédulas de R$50")
print(f"Total de {vinte} cédulas de R$20")
print(f"Total de {dez} cédulas de R$10")
print(f"Total de {um} cédulas de R$1")
