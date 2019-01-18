
x= 0
pessoas = [] # lista neste vai estar vazia

while x < 4:
    nome = input("Digite o seu nome")
    pessoas.append(nome)
    x = x +1
    #print(pessoas) para mostrar tudo ao final basta apenas tirar a adiantação
    # opção do x=x+1 é o operador += ficando x+=1
print(pessoas)