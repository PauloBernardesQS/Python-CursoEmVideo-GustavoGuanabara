
cidade = 0
cidadef = 0
maioridade = 0
homemvelho = ""
cidadef = 0
for p in range(1,5):
    print(f"-----------PESSOA {p}----------")
    nome = input("NOME: ")
    idade= int(input("IDADE: "))
    sexo= input("SEXO: ").upper()
    cidade = cidade + idade
    if p ==1 and  sexo == "M":
        maioridade = idade
    if idade > maioridade and sexo =="M":
        maioridade = idade
        homemvelho = nome
    if sexo == "F" and idade < 20:
        cidadef = cidadef + 1

print(f'''A média de idade do grupo é: {cidade/4} anos 
O nome do homem mais velho é {homemvelho} 
Existem {cidadef} mulheres que têm menos de 20 anos.''')
