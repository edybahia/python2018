
#criando a tupla
# Lista, tem a possibilidade de ser mudada os seus valores que estão guardados,
# neste caso estes ela e mutada, sendo assim posso alocar qualquer conteudo lá dentro

# Já as TUPLAs, são valores fixos sem possibilidade de mudanças.

# Comando Len checa quantos caracter tem dentro de um TUPLA print(len(mes))


mes = ('Janeiro','Fevereiro','março','abrir','maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

#neste ponto e solicitado um pedido para o usuário digitar a data de nascimento no formato. lembrando que Python, associa este
# tipo de comando como resposta INPUT. logo no padrão é um string que posso manipular, isso que eu faço a seguir
ano = input('Digite o ano do seu nascimento DD-MM-AAAA:  ')

# comando ano[3:5], pega extamente o valor entre -    - no caso o mês
# Em seguida tenho que associar este valor como inteiro, para que possa ser interpretado pelo comando seguinte e "visitar" a lista
# mes( variavel) como está sendo númerico então ele vai buscar na LISTA mes o valor do mês
# Porém a lista começa de 0 - 11, então preciso diminuir (-1) para acertar sempre o mês

print('Voce nasceu no mês de ', mes[int(ano[3:5])-1])



