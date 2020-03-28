import random

print("Jogo dos Numeros")
print("=*=*"*3)
print("1. Iniciar")
print("2. Sair")
print("=*=*"*3)

opcao = int(input("Qual a sua Opcao:"))
if(opcao == 1):
  #jogar
  tenta = [1, 2, 3]
  sort = random.randint(1, 100)
  print(sort)
  print('Vc Tem 3 Tentativas...')
  for i in tenta:
    print("Essa é sua tentativa {}".format(i))
    num = int(input("Qual numero vc acha que é:"))
    if(sort == num):
      print("Acertou!, Miserave")
      break
    elif(num > sort):
      print("MAIOR!!!!")
    else:
      print("MENOR!!!!")
elif(opcao == 2 ):
  print("Uma pena")
if(sort != num):
  print('Acabou suas Tentativas, Vc Perdeu.')
