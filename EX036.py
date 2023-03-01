numInt = int(input("Digite um numero inteiro:"))
print("="*30)
print('''VOCE DESEJA CONVERTER PARA:
[1] BINARIO
[2] OCTAL
[3] HEXADECIMAL''')
print("="*30)
opcao = int(input("Digite sua opção: "))
if opcao == 1:
 print(f"{numInt} convertido para BINARIO é igual a: {bin(numInt)[2:]}")
elif opcao == 2:
 print(f"{numInt} convertido para OCTAL é igual a: {oct(numInt)[2:]}")
elif opcao == 3:
 print(f"{numInt} convertido para HEXADECIMAL é igual a: {hex(numInt)[2:]}")
else:
 print("Opção invalida.")
