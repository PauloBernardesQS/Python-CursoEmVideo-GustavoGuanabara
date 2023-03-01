from time import sleep

def cont10():
    for c in range(0,11):
        print(f"{c}", end=" ")
        sleep(0.5)
    print("\n")
def cont0():
    for c in range(10,0,-2):
        print(f"{c}", end=" ")
        sleep(0.5)
    print("\n")
def contu():
    i = int(input("Inicio: "))
    f = int(input("Fim: "))
    p = int(input("Passo: "))
    for c in range(i, f, p):
        print(f"{c}", end=" ")
        sleep(0.5)
    print("\n")

cont10()
cont0()
contu()