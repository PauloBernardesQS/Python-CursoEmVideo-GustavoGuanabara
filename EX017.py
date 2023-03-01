import math
a = float(input("Digite o valor do angulo: "))
seno = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tang = math.tan(math.radians(a))
print(20 * "=")
print("O valor do SENO = {:.2f}".format(seno))
print("O valor do COSSENO = {:.2f}".format(cos))
print("O valor da TANGENTE = {:.2f}".format(tang))
print("=" * 20)



