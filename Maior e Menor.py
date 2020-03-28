n1 = int(input("Digite o Valor do primeiro número: "))
n2 = int(input("Digite o Valor do segundo número: "))
n3 = int(input("Digite o Valor do terceiro número: "))
menor = n1
if (n2 < n1 and n2 < n3):
  menor = n2
elif (n3 < n1 and n3 < n2):
  menor = n3
maior = n1
if (n2 > n1 and n2 > n3):
  maior = n2
elif (n3 > n1 and n3 > n2):
  maior = n3
print("O Menor valor digitado foi {}".format(menor))
print("O Maior valor digitado foi {}".format(maior))
