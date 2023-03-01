import datetime
anoNasc = int(input("Digite seu ano de nascimento: "))
ano = datetime.date.today().year
idade = ano - anoNasc
if idade <= 9:
    print("\033[31mCATEGORIA MIRIM\033[m")
elif idade > 9 and idade <= 14:
    print("\033[32mCARTEGORIA INFANTIL\033[m")
elif idade > 14 and idade <= 19:
    print("\033[33mCATEGORIA JUNIOR\033[m")
elif idade == 20:
    print("\033[34mCATEGORIA SÊNIOR\033[m")
else:
    print("\033[35mCATEGORIA MASTER\033[m")