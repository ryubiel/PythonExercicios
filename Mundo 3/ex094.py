#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade
# C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
pessoa = {}
galera = []
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Nome: "))
    while True:
        sexo = str(input("Sexo: [M/F] ")).upper()[0]
        if sexo in "MF":
            break
        print("Erro! Por favor, digite apenas M ou F")
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        escolha = str(input("Quer continuar? [S/N] ")).upper()[0]
        if escolha in "SN":
            break
        print("Erro! Por favor, digite apenas S ou N")
    if escolha == "N":
        break
print("-=" * 30)
print(f"A) Ao todo temos {len(galera)} pessoas cadastradas.")
média = soma / len(galera)
print(f"B) A média de idade é de {média:5.2f} anos.")
print("C) as mulheres cadastradas foram ", end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f"{p['nome']} ", end='')
print()
print("D) Lista das pessoas que estão acima da média: ", end='')
for p in galera:
    if p['idade'] >= média:
        print("     ", end='')
        for k, v in p.items():
            print(f"{k} = {v}; ", end='')
        print()
print("<< ENCERRADO >>")
