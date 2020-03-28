#Questão 1
text1 = str(input("Digite alguma palavra: "))
print('')
text2 = str(input("Digite alguma palavra: "))
print('')
print(f'você digitou, {text1}')
print('')
print(f'você tambem digitou, {text2}')
t = len(text1)
t1 = len(text2)
print('')
print(f'A primeira palavra que você digitou tem {t} letras')
print('')
print(f'segunda palavra que você digitou tem {t1} letras')
if (t != t1):
  print('')
  print("As duas strings são de tamanhos diferentes.")
if (text1 != text2):
  print('')
  print("As duas stings possuem conteúdo diferente.")
  print('')

#Questão 2
nome = str(input("Digite Algo: ")).upper()
taman = len(nome)
indi = taman -1
while (indi >= 0):
  print(nome[indi])
  indi -= 1

#Questão 3
nome = str(input("Digite Algo: ")).upper()
for n in nome:
  print(n)

#Questão 4
nome = str(input("Digite alguma palavra: "))
t = len(nome)-1
c = 1
while (t >= 0):
  print(nome[:c])
  t -= 1
  c += 1

#Questão 5
nome = str(input("Digite Alguma palavra: "))
t = len(nome)
while (t >= 0):
  print(nome[:t])
  t -= 1

#Questão 6
nascimento = input("Digite sua data de nascimento: ").split("/")
data1 = int(nascimento[0])
data2 = int(nascimento[1])
data3 = int(nascimento[2])
mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
print(" ")
print(f" Você nasceu em {data1} de {mes[data2 - 1]} de {data3}")

#Questão 7
frase = str(input("Digite uma frase:")).lower()
E = 0
V = 0
for n in frase:
  if (n == " "):
    E += 1
  if ( n in 'aeiou'):
    V += 1
print(E)
print(V)

#Questão 8
str1 = str(input())
str2 = str1.split()
str2 = ''.join(str2)
str3 = []
for i in range(len(str2) - 1, 0 - 1, -1):
  str3.append(str2[i])
str3 = ''.join(str3)
if str2 == str3:
  print('Palíndromo')
else:
  print('Não é')

#Questão 9
cpf = input("cpf(xxx.xxx.xxx-xx): ")
for n in cpf:
	if (cpf[3] != "." and cpf[6] != "." and cpf[11] != "-"):
		cpf = input("O cpf precisa está nesse formato(xxx.xxx.xxx-xx): ")
	else: 
		print("Cpf Válido!")
		break

#Questão 10
Tufla = ('um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte','vinte e um','vinte e dois','vinte e tres','vinte e quatro','vinte e cinco','vinte e seis','vinte e sete','vinte e oito','vinte e nove','trinta','trinta e um','trinta e dois','trinta e tres','trinta e quatro','trinta e cinco','trinta e seis','trinta e sete','trinta e oito','trinta e nove','quarenta','quarenta e um','quarenta e dois','quarenta e tres','quarenta e quatro','quarenta e cinco','quarenta e seis','quarenta e sete','quarenta e oito','quarenta e nove','cinquenta','cinquenta e um','cinquenta e dois','cinquenta e tres','cinquenta e quatro','cinquenta e cinco','cinquenta e seis','cinquenta e sete','cinquenta e oito','cinquenta e nove','sessenta','sessenta e um','sessenta e dois','sessenta e tres','sessenta e quatro','sessenta e cinco','sessenta e seis','sessenta e sete','sessenta e oito','sessenta e nove','setenta','setenta e um','setenta e dois','setenta e tres','setenta e quatro','setenta e cinco','setenta e seis','setenta e sete','setenta e oito','setenta e nove','oitenta','oitenta e um','oitenta e dois','oitenta e tres','oitenta e quatro','oitenta e cinco','oitenta e seis','oitenta e sete','oitenta e oito','oitenta e nove','noventa','noventa e um','noventa e dois','noventa e tres','noventa e quatro','noventa e cinco','noventa e seis','noventa e sete','noventa e oito','noventa e nove')
while (True):
  numero = int(input('Digite um numero de 1 a 99: '))
  if 0 <= numero <= 99:
    print(f"Você digitou o número {Tufla[numero-1]}")
    break
