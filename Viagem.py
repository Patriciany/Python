dis = float(input("Qual é a distância da Viagem?"))
print(" ")
para = int(input("Quantas paradas o ônibus irá fazer?"))
if(dis <= 250):
  preco = dis * 1.10
elif(dis > 250):
  preco = dis * 0.55
if(para > 1):
  fim = para * 1.50
elif(para <= 1):
  fim = para * 3.00
passagem = preco + fim
print(" ")
print("E o preço da sua Viagem será de R${:.2f}".format(passagem))
