import random
from arvore_binaria import Arvore_busca

random.seed(77)
lista = random.sample(range(1, 1000), 42)
ab = Arvore_busca()

for i in lista:
    ab.inserir(i)

ab.em_ordem()
print('')
encontrar = [1, 3, 981, 510, 1000]
for y in encontrar:
    v = ab.busca(y)
    if v is None:
        print(f'{y} Não foi encontrado na árvore')
    else:
        print(f'{y} Encontrado')