cores = {
    'acabar':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
    'roxo' : '\033[35m'
}
n1 = float(input("Digite o valor do primeiro numero: "))
n2 = float(input("Digite o valor do segundo numero: "))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
pot = n1 ** n2
divint = n1 // n2
e = n1 % n2
print(f"{cores['verde']}A soma dos numero é igual a{cores['acabar']} {cores['vermelho']}{soma}{cores['acabar']}{cores['verde']},  A subtração é {cores['acabar']} {cores['vermelho']}{sub}{cores['acabar']}{cores['verde']}, A multiplicação é{cores['acabar']} {cores['vermelho']}{mult}{cores['acabar']}{cores['verde']}, A divisão{cores['acabar']} {cores['vermelho']}{div:.2f} {cores['acabar']}")
print("A potencia é {:.3f}, A divisao inteira é {}, E o que sobrou da div inteira é {}".format(pot, divint, e))
