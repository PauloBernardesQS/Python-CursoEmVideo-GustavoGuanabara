largura = float(input("Qual o tamanho da largura da sua parede: "))
altura = float(input("Qual o tamanho da altura da sua parede: "))
area = largura * altura
tinta = area / 2
print("Voce vai precisar de {} litros de tinta para pintar {}m²".format(tinta, area))
