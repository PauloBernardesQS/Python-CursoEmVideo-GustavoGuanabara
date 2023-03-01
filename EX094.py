dados = dict()
pessoas = list()
soma = 0
mulheres = list()
acimaMedia = list()

while True:
    dados.clear()
    dados['nome'] = (input("Nome: "))
    while True:
        dados['sexo'] = input("Sexo(M/F): ")
        if dados['sexo'].upper() == 'M' or dados['sexo'].upper() == 'F':
            break
        else:
            print("Sexo invalido. Digite novamente...")
            continue
    if dados['sexo'].upper() == 'F':
        mulheres.append(dados['nome'])
    dados['idade'] = int(input("Idade: "))
    soma += dados['idade']
    pessoas.append(dados.copy())
    while True:
        continuar = input("Voce deseja continua(S/N): ")
        if continuar.upper() == "S" or continuar.upper() == "N":
            break
        else:
            print("Opção invalida, digite novamente...")
            continue
    if continuar.upper() == "S":
        continue
    else:
        break

print(pessoas)
media = soma / len(pessoas)
print(f'''
Foram cadastradas {len(pessoas)} pessoas
Ao todo elas possuem {soma} anos
A media de idade é de {media}
Mulheres presentes: {mulheres}
''')
for m in pessoas:
    if dados['idade'] >= media:
        acimaMedia.append(dados['nome'])
        print(f"Pessoas com idade acima da media {acimaMedia}")
