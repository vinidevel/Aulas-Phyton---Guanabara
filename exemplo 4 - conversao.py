num = int(input("Digite um número inteiro:"))
print(""" Escolha uma das bases para conversão:
    {1} Binário
    {2} Octal
    {3} Hexadecimal""")
opcao = int(input("Sua opção:"))
if opcao == 1:
    print("{} convertido para Binário é igual a {}".format(num, bin(num)))
elif opcao == 2:
    print("{} convertido para Octal é igual a {}".format(num, oct(num)))
elif opcao == 3:
    print("{} convertido para Hexadecimal é igual a {}".format(num, hex(num)))
else:
    print("Opção invalida")