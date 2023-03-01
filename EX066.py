while True:
    nT = float(input("Voce quer ver a tabuada do numero (numeros negativos quebram o loop) -> "))
    if nT < 0:
        break
    print("-=" * 20)
    for c in range(1, 11):
        print(f"{nT} X {c} = {nT * c}")
    print("-=" * 20)