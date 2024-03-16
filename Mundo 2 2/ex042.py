print("-=" * 20)
print("Analisador de Triângulos")
print("-=" * 20)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR triângulo")
    if r1 == r2 == r3:
        print("Forma o triângulo equilátero")
    elif r1 != r2 != r3 != r1:
        print("Forma um triângulo escaleno")
    else:
        print("Forma um triângulo isósceles")
else:
    print("Os segmentos acima NÃO PODEM FORMAR triângulo")