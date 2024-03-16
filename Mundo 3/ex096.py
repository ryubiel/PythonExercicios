#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def área(larg, comp):
    terreno = larg * comp
    print(f"A área de um terreno {larg}X{comp} é de {terreno}m2.")

print(" Controle de Terrenos")
print("-" * 20)
largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))
área(largura, comprimento)