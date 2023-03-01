import datetime
anoNasc = int(input("Digite seu ano de nascimento: "))
ano = datetime.date.today().year
idade = ano - anoNasc
if idade == 18:
    print("Esta na hora de se alistar")
elif idade > 18:
    print(f"Se passou {idade - 18} anos do tempo de alistamento")
else:
    print(f"Faltam {18 - idade} anos para poder se alistar")

