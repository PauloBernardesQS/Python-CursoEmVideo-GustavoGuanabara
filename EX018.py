from random import choice
a1, a2, a3, a4 = input("Nome 1° Aluno: "), input("Nome 2° aluno: "), input("Nome 3° aluno: "), input("Nome 4° aluno: ")
lista = [a1, a2, a3, a4]
print("O aluno sorteado foi {}".format(choice(lista)))
