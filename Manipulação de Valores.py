n1 = int(input("Primeiro Valor:"))
n2 = int(input("Segundo valor:"))
opção = 0
while(opção != 5):
  print('''  [1] Somar  
  [2] multiplicar
  [3] maior
  [4] outros valores
  [5] Sair do programa''')
  opção = int(input("Qual é a sua opção:"))
  if(opção == 1):
    valor1 = n1 + n2
    print(" O resoltado é {}".format(valor1))
  elif(opção == 2):
    valor2 = n1 * n2 
    print("O valor da Multiplicação é {}".format(valor2))
  elif(opção == 3 ):
    if(n1 > n2):
      maior = n1
    else:
      maior = n2
    print("O maior valor é {}".format(maior))
  elif(opção == 4):
    print("Informe novos valores:")
    n1 = int(input("Primeiro Valor:"))
    n2 = int(input("Segundo Valor:"))
  elif(opção == 5):
    print("Finalizando o Programa...")
  else:
    print("Valor Invalido.")
