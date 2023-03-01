salario = float(input("Digite o valor do seu salario: "))
if salario > 1250:
    print(f"Seu novo salario vai ser R${salario+(salario*0.10):.2f} ")
else:
    print(f"Seu novo salario vai ser de R${salario+(salario*0.15):.2f}")