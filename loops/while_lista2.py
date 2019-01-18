
x= 0
pessoas = [] # lista neste vai estar vazia

while x < 4: # neste laço o loop continua até encontrar a palavra João, joão não é para entrar na lista
    nome = input("Digite o seu nome")
    if nome == "joao":
        continue        #quando o compilador encontra este palavra joão ele volta para o inicio do while, ou seja não
                        # executaa o pessoas.append(nome)
                        # substituir continue por break tem a possibilidade de sair com o loop imediatamente
    pessoas.append(nome)
    x +=1
print(pessoas)

# neste codigo vair ter um erro pois joão entra na lista, prox codigo pode ser atualizado sem este erro
