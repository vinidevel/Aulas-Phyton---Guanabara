nota1 = int(input('Digite sua primeira nota:'))
nota2 = int(input('Digite sua segunda nota:'))
media = (nota1 + nota2)/2
if media > 5:
    print("Parabéns ! Você está aprovado com a média {}".format(media))
elif media < 5:
    print("Infelizmente você não oteve pontos suficientes alcançando uma média {}. Está em recuperação.".format(media))