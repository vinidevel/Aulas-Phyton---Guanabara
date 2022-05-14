from datetime import date
anoAtual = date.today().year
anoNasc = int(input("Digite o ano de seu nascimento:"))
idade = anoAtual - anoNasc
if idade <= 12:
    print("Você tem {} anos e pertence a categoria baby".format(idade))
elif idade <= 19:
    print("Você tem {} anos e pertence a categoria Senior".format(idade))
elif idade >= 20:
    print("Você tem {} anos e pertence a categoria Pleno".format(idade))