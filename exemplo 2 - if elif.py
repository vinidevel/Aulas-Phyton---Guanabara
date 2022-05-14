nome = str(input("Digite qual é o seu nome")).strip().lower()
if nome == "vini":
    print("Que lindo nome !")
elif nome == "pedro" or nome == "paula" or nome == "joao":
    print("Seu nome é bem comum, {}".format(nome))
else:
    print("Nunca ouvi este nome antes, {}".format(nome))