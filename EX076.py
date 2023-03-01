palavras = ("tubarão","uva","marcauja","casacao","pefew","wvvev","tuvsaddsbarão")
for e in palavras:
    print(f"\nNa palavra {e} temos", end= " ")
    for letra in e:
        if letra.lower() in "aeiou":
            print(f"{letra}", end=' ')