import datetime
ano = datetime.date.today().year
s= 0
for c in range(0, 7):
    dataNasc = int(input("Seu ano de nascimento: "))
    if ano - dataNasc >= 21:
        s = s+1
print(f"\033[32mDE 7 PESSOAS \033[m\033[31m{s}\033[m \033[31mSÃO MAIORES DE IDADE")
