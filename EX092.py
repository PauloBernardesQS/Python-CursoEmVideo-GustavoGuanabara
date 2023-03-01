from datetime import datetime

dados = dict()
dados['nome'] = input("Digite seu nome -> ")
anonasc = int(input("Digite seu ano de nascimento -> "))
dados['idade'] = datetime.today().year - anonasc
dados['carteira'] = int(input("Digite o numero da sua carteira de trabalho, se não possui digite 0 -> "))
if not dados['carteira'] == 0:
    dados['contratacao'] = int(input("Digite seu ano de contratação -> "))
    if datetime.today().year - dados['contratacao'] >= 20:
        aposentadoria = "Aprovada"
    else:
        aposentadoria = datetime.today().year - dados['contratacao']
    dados['Salario'] = float(input("Digite seu salario -> R$"))
    print(f''' 
    Nome: {dados['nome']}
    Idade: {dados['idade']}
    Carteira de Trabalho: {dados['carteira']}
    Ano de contratação: {dados['contratacao']}
    Salario: {dados['Salario']}
    ''')
    if aposentadoria == 'Aprovada':
        print(f"Aposentadoria: {aposentadoria}")
    else:
        print(f'Aposentadoria: Faltam {aposentadoria} anos')
else:
    print(f'''Nome: {dados['nome']}
    Idade: {dados['idade']}
    Carteira de Trabalho: Não possui''')