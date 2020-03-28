perguntas = ["Telefonou para a vítima?","Esteve no local do crime?"
,"Mora perto da vítima?", "Devia para a vítima?",
"Já trabalhou com a vítima?"]
resp = s = 0
for p in perguntas:
  resp = str(input(f"{p} [Sim/Não]: ")).lower()
  if (resp in "sim"):
    s += 1
if (s == 2):
  print("Suspeito")
elif( 3 <= s <= 4):
  print("Cúmplice")
elif( s == 5):
  print("Assasino")
else:
  print("Inocente")
