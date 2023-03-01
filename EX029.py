n = int(input("\033[4;34mDigite um numero inteiro:\033[m "))
pi = n%2
if pi == 1:
    print(f"{n} é impar")
else:
    print(f"{n} é par")