#Questão 1
alunos=["Adnilton", "Alcymara", "Allan",\
"Ana Carolina", "Ana Julia", "Anderson", "Andre"]
while True:
  professor = str(input())
  if professor in "FIM":
    break
  elif professor in alunos:
    print("PRESENTE")
  else:
    print("AUSENTE")

#Questão 2
clientes = []
idades = []
op = int(input())
while(op != -1):
  if(op == 1):
    nome, idade = input().split()
    clientes.append(nome)
    idades.append(idade)
  elif(op == 2):
    if(len(clientes) > 0):
      print(clientes[0], idades[0])
      clientes.pop(0)
      idades.pop(0)
    else:
      print("VAZIO")
  elif(op == 3):
    idadesaux = idades.copy()
    idadesaux.sort(reverse = True)
    clientesaux = []
    for i in idadesaux:
      pos = idades.index(i)
      idades.pop(pos)
      nome = clientes.pop(pos)
      clientesaux.append(nome)
    clientes = clientesaux.copy()
    idades = idadesaux.copy()
  op = int(input())

#Questão 3
lista = list()
while True:
  per = str(input())
  if per == 'FIM':
    break
  lista.append(per)
  lista.sort()
  for i in lista:
    print(i)
  print("--FIM--")

#Questão 4
lista = ["Pedro", "Adnilton", "Alcymara", "Jose", "Allan","Bastiao", "Ana Carolina", "Ana Julia", "Severino", "Anderson", "Andre"]
while(len(lista)):
  per = int(input())
  if(per > len(lista)):
    print("--ALEM DO ULTIMO--")
  elif(not lista):
    break
  else:
    Remo = lista.pop(per)
    print(Remo)
