from random import randint 
from time import sleep
comp = randint(0, 10)
print("Sou seu computador...")
sleep(1)
print("Acabei de pensar em número entre 0 e 10.")
sleep(1)
print("Será que vc consegue adivinha?")
sleep(1)
acert = False
pal = 0
while(not acert):
  usuario = int(input("Qual o seu palpite? "))
  pal += 1
  print("Errou, Tente de Novo")
  print(' ')
  if(usuario == comp):
    acert = True
print("Acertou com {} tentativas, parabens".format(pal))
