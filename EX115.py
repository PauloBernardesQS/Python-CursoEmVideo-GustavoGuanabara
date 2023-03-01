from ex115.Interface import *
from ex115.Arquivos import *
from time import sleep
arquivo = "cadastro.txt"
initArq(arquivo)

while True:
    sleep(1)
    x = menu(["Cadastrar", "Ver Cadastros", "Sair"])
    if x == 1:
        addP(arquivo)
    elif x == 2:
        sleep(1)
        lerArq(arquivo)
        continue
    elif x == 3:
        print(cabecalho("Opcao 3"))
        exit()
    else:
        print("Opção Invalida.")
        continue
