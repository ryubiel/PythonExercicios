l = float(input("Largura da parede: "))
a = float(input("Altura da parede: "))
m2 = l * a
print("Sua parede tem a dimensão de {}X{} e sua área é de {}m².".format(l,a,m2))
print("Para pintar essa parede, você precisará de {}l de tinta".format(m2 / 2))