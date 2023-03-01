from ex115.Interface import *

def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
        print(f"Arquivo {nome} Encontrado")
    except FileNotFoundError:
        return False
    else:
        return True

def criarArq(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        (f"Não foi possivel criar o arquivo {nome}")
    else:
        print("Arquivo Criado")

def initArq(nome):
    a = arqExiste(nome)
    if a == False:
        criarArq(nome)

def lerArq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Erro ao Ler Arquivo")
    else:
        print(cabecalho("Pessoas"))
        for lista in a:
            dados = lista.split(";")
            print(f"Nome: {dados[0]:<30} {'Idade:':>3} {dados[1]}")
        a.close()

def addP(nome):
    print(cabecalho("NOVO CADASTRO"))
    name = input("Nome: ")
    idade = LeiaInt("Idade: ")
    try:
        a = open(nome, 'at')
        a.write(f'{name};{idade} \n')
    except:
        print("Erro ao cadastrar")
    else:
        print("Cadastro feito com sucesso!")
        a.close()

