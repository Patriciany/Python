from random import randint
from time import sleep
print("Vou Pensar em um número de 0 à 100. Tente adivinhar ")
sleep(3)
print(' ')
sorteio = randint(0,100)
jogo = int(input("Em que numero eu pensei? "))
ant = sorteio - 10
post = sorteio + 10
print(" ")
print(">>>>CARREGANDO>>>>")
print(" ")
sleep(5)
if(jogo == sorteio):
  print("Você acertou o desafio!.")
elif(jogo >= ant and jogo <= post):
  print("Você está quente. Quase acertou!")
else:
  print("Você está frio. Nem chegou perto!")
sleep(3)
print(' ')
print(f"O numero que eu pensei foi {sorteio}")
