import random
from arvore_binaria import Arvore_busca, No

random.seed(25)
lista = random.sample(range(1, 1000), 50)
ab = Arvore_busca()

for i in lista:
    ab.inserir(i)

ab.em_ordem()
print('')
encontrar = [1, 220, 36, 997, 880, 800]
for y in encontrar:
    v = ab.busca(y)
    if v is None:
        print(f'{y} Não foi encontrado na árvore')
    else:
        print(f'{v.raiz.dado} Encontrado')

print(f'O nó de menor valor é: {ab.minimo()}')
print(f'O nó de maior valor é: {ab.maximo()}')

print(f'O número total de nós é: {ab.total_nos()}')
print(f'O número total de folhas é: {ab.total_folhas()}')

print(f'A altura da árvore é de {ab.altura()} nós')

ab.remover(220)
ab.em_ordem()
