# dados do usuario (nome, nota prova 1, nota prova 2 e total de faltas

nome = input("Digite o seu nome")
np1= int(input("Digite a nota da prova 1"))
np2= int(input("Digite a nota da prova 2"))
faltas= int(input("Digite o total de faltas"))

media = float((np1+np2)/2)
faltou = float((faltas/20)*100)

print(nome)
print("Sua média na disciplina é de %f" %(media))
print("Sua assiduidade na disciplina é de %d " %(faltou))

if faltou >= 30 and media <= 5.9:
    print("reprovado por falta e por média")

elif faltou >= 30:
    print("reprovado por faltas")

elif faltou <= 30 and media <= 5.9:
    print("reprovado por média")

else:
    print("Aprovado")
