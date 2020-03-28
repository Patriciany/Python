num = [5, 8, 3, 10, 5]
tama = len(num)
ind = 0
soma = 0
maior = 0
mediapro = 0
while(ind <= tama-1):
  print(num[ind], end= " ")
  soma += num[ind]
  media = soma / tama
  if(num[ind] > maior):
    maior = num[ind]
  ind += 1
print('=',soma)
print("Maior Valor =",maior)
print("A Media foi =", media)
nume = num[0]
ocorrecia = num.count(nume)
print("O numero de orrência do valor {} apareceu {} vezes".format(nume, ocorrecia))
