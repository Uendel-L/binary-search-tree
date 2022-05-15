import random
from arvore_binaria import Arvore_busca

lista = random.sample(range(1, 100), 20)
ab = Arvore_busca()
for i in lista:
    ab.inserir(i)
