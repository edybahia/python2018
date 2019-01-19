
fatura = [] #criando a lista
repetir = "s"
total = 0
validado = False

while repetir == 's':
    venda = input("Digite a sua mercadoria")

    #validando dados com try e exibindo resposta com except
    while validado == False:
        preco = input("Digite o preço")
        try:
            preco = float(preco)
            if preco <=0:
                print('Preco tem que ser maior que 0')
            validado = True
        except:
            print("Formato do dado invalido use numeros apenas")

    fatura.append([venda,preco])      #criando uma lista dentro da lista para organizar melhor
    total += preco
    validado = False  # Volta para False para manter o loop
    repetir = input("Voce que comprar mais produtos [S ou N]").lower()

for i in fatura: # for para exibir os valores da lista salvos, por ser apenas 2 itens o for vai imprimir na seq
    print(i[0], '-', i[1])

print('O total da fatura é :',total)