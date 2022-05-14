nome = str(input("Digite qual é o seu nome")).strip().lower()
if nome == "vini":
    print("Que lindo nome !")
else:
    print("Seu nome é bem comum")
    print("Tenha um bom dia, {}".format(nome))