n1 = float(input("Quanto voce tirou na sua primeira prova ? "))
n2 = float(input("Quanto voce tirou na sua segunda prova ? "))
media = ((n1 + n2) / 2)
print(f"Media = {media}")
if media < 5:
    print("\033[31mReprovado\033[m")
elif media >= 5 and media <= 6.9:
    print("\033[34mRecuperação\033[m")
elif media >= 7:
    print("\033[32mAprovado\033[m")