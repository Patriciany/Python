import random
print("=-"*25)
print("Vou pensar em um número de 0 à 5. Tente adivinhar")
print("=-"*25)
jogo = int(input("Em que número eu pensei? "))
print("=-"*13)
lista = [0, 1, 2, 3, 4, 5]
sorteio = random.choice(lista)
print(f"Eu Pensei em {sorteio}")
print("=-"*7)
if(jogo == sorteio):
  print("Acertou Mizerave!")
else:
  print("Errou de Lasco!") 
print("=-"*7)
