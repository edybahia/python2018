# lower() para que seja possivel entender apenas as minusculas mesmo o usuario digitando maisculas
# sexo não precisa de variavel pois por padrão o pytho aceita string
# lembrar que os if no python necessita do recuo (indentado)

idade = int(input("Digite a sua idade"))
sexo = input("Digite seu sexo M ou F").lower()
cidade = input("Digite a cidade").lower()

# programa só vai odar se o usuario digitar uma ou outra cidade apresentada

if cidade == "aracaju" or cidade == "sao paulo":

    if idade < 18 and sexo == 'm':
        print(" Homem menor de idade")

    elif idade>=18 and sexo =='m':
        print("Homem maior de idade")

    elif idade < 18 and sexo =='f':
        print("Mulher menor de idade")

    elif idade >= 18 and sexo =='f':
        print("Mulher maior de idade")

    else:
        print(" Erro na entrada de dados")


else:
    print("cidade não definida")