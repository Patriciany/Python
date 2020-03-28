meu_dic = {'nome':'ota','idade':39}

#imprimir Ota
print(meu_dic['nome'])
#imprimir 39
print(meu_dic['idade'])
#Acessar uma chave que não existe retorna um erro
#meu_dic.get('endereco')
#meu_dic['endereco']
chave = str(input('Digite: '))
if(chave in meu_dic):
  print(f'{chave} Valor {meu_dic[chave]}')
else:
  print(f'{chave} Ausente')

#Atualizar idade
meu_dic['idade'] = 40

print(meu_dic)

#adicinar item
meu_dic['endereco'] = 'Jardim Cidade Universitária'

print(meu_dic)

#Remove e imprime im item 
print(meu_dic.pop('idade'))
print(meu_dic)

#Remove todos os itens método clear()
meu_dic.clear()
print(meu_dic)
