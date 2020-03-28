cA = float(input())
cO = float(input())
hi = (cO ** 2 + cA ** 2) ** (1/2)
print("A hipotenusa vai medir{:.2f}".format(hi))


from math import hypot
cA = float(input())
cO = float(input())
hi = hypot(cO, cA)
print("A hipotenusa vai medir{:.2f}".format(hi))
