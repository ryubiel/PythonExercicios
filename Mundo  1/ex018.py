from math import radians, sin, cos, tan

angulo = float(input("Digite o ângulo que você deseja: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print("O ângulo de {} tem o SENO de {:.2f}, COSSENO de {:.2f} e TANGENTE de {:.2f}".format(angulo,seno,cosseno,tangente))