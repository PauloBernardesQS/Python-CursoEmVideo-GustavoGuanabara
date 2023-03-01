def maior(* num):
    cont = maior = 0
    for m in num:
        cont +=1
        if m > maior:
            maior = m
    print(f'''
    Foram analizados {cont} numeros, sendo eles {num}.
    O maior numero analizado foi {maior}
    ''')
maior(0, 3, 434, 62, 43, 53)