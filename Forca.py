import random
sort = ["tubarao", "gafanhoto", "golfinho", "galinha", "ornitorrinco", "camelo", "escorpiao", "leao", "hiena", "aranha", "crocodilo", "elefante", "cobra", "tigre", "coruja", "cachorro", "gato", "esquilo", "preguica", "macaco", "lobo", "porco", "arara", "borboleta", "tigre de bengala", "bruno"]
palavra = random.choice(sort).lower().strip()
digitadas = []
acertos = []
erros = 0
while True:
  senha = ""
  for letra in palavra:
    senha += letra if letra in acertos else "-"
  print(senha)
  if senha == palavra:
    print("Você acertou!")
    break
  tentativa = input("Digite uma letra:").lower().strip()
  if tentativa in digitadas:
    print("Você já tentou esta letra!")
    continue
  else:
    digitadas += tentativa
    if tentativa in palavra:
      acertos += tentativa
    else:
      erros += 1
      print("Você errou pela {}ª vez. Tente de Novo!".format(erros))
  if (erros == 6):
    print("Enforcado!")
    break
	
