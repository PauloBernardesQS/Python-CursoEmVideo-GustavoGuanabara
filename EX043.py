preco = float(input("Digite o valor do produto: "))
print("="* 20)
print("Formas de pagamento:")
print("A vista no dinheiro")
print("A vista no cheque")
print("A vista no cartao")
print("2x no cartao")
print("3x no cartao")
print("=" * 20)
pagamento = (input("Qual das formas de pagamento voce ira utilizar? "))
if pagamento.upper() == "A VISTA NO DINHEIRO" or pagamento.upper() == "A VISTA NO CHEQUE":
    print(f"O preco vai cair para {preco - (preco * 0.10)}")
elif pagamento.upper() == "A VISTA NO CARTAO":
    print(f"O preco vai cair para {preco - (preco * 0.05)}")
elif pagamento.upper() == "2X NO CARTAO":
    print(f"2 parcelas de {preco / 2}")
elif pagamento.upper() == "3X NO CARTAO":
    print(f"3 parcelas de {(preco + (preco * 0.20)) / 3}")