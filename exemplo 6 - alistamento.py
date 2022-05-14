from datetime import date
anoAtual = date.today().year
anoNascimento = int(input("Digite seu ano de nascimento:"))
idade = anoAtual - anoNascimento
alistamento = 18
if idade == alistamento:
    print("Voce tem {} anos. Deve se alistar imediatamente !".format(idade))
elif idade < alistamento:
    tempoRestante = alistamento - idade
    print("Voce tem {} anos. Deve se alistar daqui a {} anos".format(idade, tempoRestante))
elif idade > alistamento:
    tempoPassado = idade - alistamento
    print("Você tem {} anos. Deveria ter se alistado há {} anos".format(idade, tempoPassado))
    
