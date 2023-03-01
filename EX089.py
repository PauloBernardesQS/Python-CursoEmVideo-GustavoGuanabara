lista = list()
while True:
    name = input("Digite o nome do aluno -> ")
    n1 = int(input("Digite a primeira nota do aluno -> "))
    n2 = int(input("Digite a segunda nota do aluno -> "))
    media = (n1 + n2) / 2
    lista.append([name,[n1,n2],media])
    continuar = input("Deseja continuar (s/n) -> ")
    if continuar == "s":
        continue
    else:
        break
for l, d in enumerate(lista):
    print(f'''CODIGO: {l}     NOME: {d[0]}       MEDIA:{d[2]}''')

verificarn = int(input("Digite o codigo do aluno para ver suas notas (999 interrompe o programa): "))
if verificarn == "999":
    exit()
else:
    if verificarn < len(lista):
        print(f"As notas de {lista[verificarn][0]} são {lista[verificarn][1]}")