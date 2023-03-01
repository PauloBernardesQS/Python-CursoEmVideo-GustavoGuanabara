def aumentar(v,a):
    porcentagem = a / 100
    aumento = v + v * porcentagem
    return moedas(aumento)

def diminuir(v,d):
    porcentagem = d / 100
    diminuicao = v - v * porcentagem
    return moedas(diminuicao)

def dobro(v):
    mult = v * 2
    return moedas(mult)

def metade(v):
    met = v / 2
    return moedas(met)

def moedas(v, moeda = "R$"):
    return (f"{moeda}{v}".replace(".",","))

def resumo(v,a,d):
    print(f'''{"-="*20} 
Dobro de {moedas(v)} = {dobro(v)}
A metade de {moedas(v)} = {metade(v)}
O aumento de {a}% de {moedas(v)} = {aumentar(v,a)}
A dinuição de {d}% de {moedas(v)} = {diminuir(v,d)}
{"-="*20}
    ''')



