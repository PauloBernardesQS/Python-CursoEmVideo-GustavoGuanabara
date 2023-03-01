from random import choice
u= (input("PEDRA, PAPEL OU TESOURA? ")).strip()
ppt = ["PEDRA", "PAPEL", "TESOURA"]
pc = choice(ppt)
print(f"VOCE ESCOLHEU {u.upper()}")
print(f"O COMPUTADOR ESCOLHEU {pc}")
if pc == "PEDRA":
    if u.upper()=="PEDRA":
        print("\033[34mEMPATE, JOGUE NOVAMENTE!")
    elif u.upper()=="PAPEL":
        print("\033[32mVOCE GANHOU!")
    elif u.upper()=="TESOURA":
        print("\033[31mVOCE PERDEU...")
    else:
        print("VALOR INVALIDO")
elif pc == "TESOURA":
    if u.upper()=="PEDRA":
        print("\033[32mVOCE GANHOU!")
    elif u.upper()=="PAPEL":
        print("\033[31mVOCE PERDEU...")
    elif u.upper()=="TESOURA":
        print("\033[34mEMPATOU, JOGUE NOVAMENTE!")
    else:
        print("VALOR INVALIDO")
elif pc == "PAPEL":
    if u.upper()=="PAPEL":
        print("\033[34mEMPATOU, JOGUE NOVAMENTE!")
    elif u.upper()=="TESOURA":
        print("\033[32mVOCE GANHOU!")
    elif u.upper()=="PEDRA":
        print("\033[31mVOCE PERDEU...")
    else:
        print("VALOR INVALIDO")
