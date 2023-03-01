vlrCasa = float(input("Digite o valor da casa desejada: R$"))
salario = float(input("Digite o valor do seu salario: R$"))
anos = int(input("Em quantos anos voce vai querer parcelar: "))
vlrMensal = vlrCasa / (anos * 12)
if vlrMensal > (salario * 0.3):
    print("\033[31mInfelizmento voce nao vai poder financiar a casa.\033[m")
else:
    print(f"\033[32mVoce podera financiar a casa em R${vlrMensal:.2f} por mes\033[m")