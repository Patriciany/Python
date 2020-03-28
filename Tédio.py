from time import sleep
for i in range(10, 0, -1):
  sleep (0.99)
  print(i)
print("Feliz Ano NOVO!")

n = 1
while(n != 0):
  n = int(input("Digite um valor, Digite[0] para parar!:"))
print("CAGUEIIIIIIIIIII...")

rep = int(input("Quantas vezes você quer repetir?"))
ini = int(input("Quer começar de onde?"))
pas = int(input("Qual é o passo?"))
for p in range (ini, rep+1, pas):
  #if(p % 2 == 0):
  print(p)

no = input("Digite o nome:")
print("{}, é um venenoza".format(no))

QA = int(input("Quantas vezes você vai querer Repetir?")) 
i = 1
for p in range (i, QA+1):
  n = input("Qual o seu Nome?")
  for o in range(1, 4):
    d = input("Qual o %d° dia que você ficar?"%(o))
