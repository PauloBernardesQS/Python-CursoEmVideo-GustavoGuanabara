colegio = dict()
colegio["aluno"] = input('Digite o nome do aluno(a) -> ')
colegio["media"] = float(input(f"Digite a media de {colegio['aluno']} -> "))
if colegio["media"] >= 6:
    colegio["resultado"] = "Aprovado(a)"
else:
    colegio["resultado"] = "Reprovado(a)"
print(f'''
Nome do aluno(a): {colegio["aluno"]}
Media de {colegio["aluno"]}: {colegio["media"]}
Situação: {colegio["resultado"]} ''')

