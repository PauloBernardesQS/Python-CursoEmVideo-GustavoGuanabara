from datetime import datetime
def voto(anonasc = datetime.today().year):
    anonasc = int(input("Ano de nascimento: "))
    idade = datetime.today().year - anonasc
    if idade < 16:
        return f"{idade} anos: Voto negado"
    if idade >= 16:
        return f"{idade} anos: Voto opcional"
    if idade >= 18:
        return f"{idade} anos: Voto obrigatorio"
print(voto())