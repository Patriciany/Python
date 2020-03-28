import random
A1 = str(input())
A2 = str(input())
A3 = str(input())
lista = [A1, A2, A3]
sorteio = random.choice(lista)
print("O Aluno escolhido foi {}".format(sorteio))

import random
A1 = str(input())
A2 = str(input())
A3 = str(input())
lista = [A1, A2, A3]
random.shuffle(lista)
print("A ordem agora é {}".format(lista))
