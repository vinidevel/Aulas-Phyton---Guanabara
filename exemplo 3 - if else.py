valorCasa = int(input("Qual é o valor da Casa ?"))
salario = int(input("Qual é seu salário ?"))
anosPrestacao = int(input("Em quantos anos pretende parcelar este imovel ?"))
calculoPrestacao = (valorCasa/anosPrestacao)/12 
print("O valor da casa é {}, o salário do cliente é {} e a prestacao para {} anos ficará em R${} mensais".format(valorCasa, salario, anosPrestacao, calculoPrestacao))
if calculoPrestacao <= 0.30*salario:
    print("Parabéns ! Você poderá financiar esta casa, pois o valor da prestação não excede 30% de sua renda.")
else:
    print("Infelizmente não será possível aprovar este financiamento, pois o valor da prestação excede 30% da sua renda.")