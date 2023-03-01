def fatorial(num, show=False):
    '''

    :param num: Numero fatoriado
    :param show: Mostrar o caminho da fatoriação (False/True)
    :return: Retorna o resultado da fatoração
    '''
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(f"{c}", end="")
            if c > 1:
                print(" X ",end='')
            else:
                print(" = ", end="")
    return f
print(fatorial(3,True))