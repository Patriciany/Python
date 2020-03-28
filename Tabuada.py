cont = 'S'
while(cont == "S"):
  mult = 1
  multi = int(input("Qual o valor que Vc quer Multiplicar?"))
  while(mult <= 10):
    prod = mult * multi
    print("{} x {} = {}".format(mult, multi, prod))
    mult += 1
  cont = input("Voçe quer continuar? (S/N):").upper()
