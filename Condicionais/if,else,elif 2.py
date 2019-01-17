# lower() para que seja possivel entender apenas as minusculas mesmo o usuario digitando maisculas
# sexo não precisa de variavel pois por padrão o pytho aceita string

idade = int(input("Digite a sua idade"))
sexo = input("Digite seu sexo M ou F").lower()

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