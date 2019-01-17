
categoria= int(input("Digite a categoria do produto"))

if categoria ==1:
    preco =10

elif categoria ==2:
    preco =18

elif categoria ==3:
    preco =23

elif categoria ==4:
    preco =26

else:
    print("Produto fora da lista")
    preco=0

print("O preço é %d" %preco)