r1 = float(input("Primeira Reta:"))
r2 = float(input("Segunda Reta:"))
r3 = float(input("Terceira Reta:"))
if(r1 <= r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2):
  print("As Retas acima podem formar um Triângulo")
else:
  print("As Retas acima não podem formar um Triângulo")
