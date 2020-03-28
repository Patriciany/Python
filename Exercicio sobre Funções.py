#Questão 1
def CalcularAreaTerreno(Largura, Comprimento):
  Area = Largura * Comprimento
  return Area
x = float(input("Base: "))
y = float(input("Altura: "))
A = CalcularAreaTerreno(x, y)
print(A)

#Questão 2
def CalcularMetroCentimetro(Metro):
  Centrimento = Metro * 100
  return Centrimento
x = float(input("Metros: "))
C = CalcularMetroCentimetro(x)
print(C)

#Questão 3
def CalcularSegundos(dias, horas, minutos):
  SegundosDias = dias * 86400
  SegundosHoras = horas * 3600
  SegundosMinutos = minutos * 60
  soma = SegundosDias + SegundosHoras + SegundosMinutos
  return soma
x = int(input("Dias: "))
y = int(input("Horas: "))
z = int(input("Minutos: "))
segundos = CalcularSegundos(x, y, z)
print(segundos)

#Questão 4
def escrever(textual):
  texto = textual
  return texto
x = str(input("Escreva: "))
texto = escrever(x)
print("-"*15)
print(texto)
print("-"*15)

#Questão 5
def contador(inicio, fim, passo):
  print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
  cont = inicio
  while(cont <= fim):
    print(f"{cont}", end=' ')
    cont += passo

contador(1, 10, 1)
contador(10, 1000, 10)

#Questão 6
def tempoViagemCarro(distâcia, velocidade):
  tempo = distâcia / velocidade
  return tempo
x = int(input("Distância: "))
y = int(input("Velocidade: "))
tempo = tempoViagemCarro(x, y)
print(tempo)

#Questão 7
def calcularCelsiusFahrenheit(celsius):
  fahrenheit = (9 * celsius / 5 + 32)
  print(fahrenheit)
x = float(input("Celsius: "))
calcularCelsiusFahrenheit(x)

#Questão 8
def calcularAlguelCarro(dias, km):
  dias *= 60.00
  km *= 0.15
  valorPagar = dias + km
  return valorPagar
x = int(input("Dias: "))
y = int(input("Km: "))
total = calcularAlguelCarro(x, y)
print("R${:.2f}".format(total))
