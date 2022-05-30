import random

#random.seed(25)
lista = [1,2,3] #random.sample(range(1, 1000), 50)
ab = Arvore_busca()

for i in lista:
    ab.inserir(i)

print('Exibindo árvore em Ordem')
ab.em_ordem()
print('\nExibindo árvore em Pré Ordem')
ab.pre_ordem()
print('\nExibindo árvore em Pós Ordem')
ab.pos_ordem()
print('\nEfetuando Busca')
encontrar = [1, 220, 3, 997, 2, 800]
for y in encontrar:
    v = ab.busca(y)
    if v is None:
        print(f'{y} Não foi encontrado na árvore')
    else:
        print(f'{v.raiz.dado} Encontrado')

print(f'O nó de menor valor é: {ab.minimo()}')
print(f'O nó de maior valor é: {ab.maximo()}')

print(f'O número total de nós é: {ab.total_nos()}')
print(f'As folhas da Arvore são: ', end='')
print(f'\nO número total de folhas é: {ab.total_folhas()}')

valor = 3
altura = ab.altura(valor)
if altura is None:
    print(f'O valor {valor} não está contido na Árvore')
else:    
    print(f'A altura da nó é: {altura}')

valor = 3
nivel = ab.nivel(valor)
if nivel is None:
    print(f'O valor {valor} não está contido na Árvore')
else:    
    print(f'O nivel da nó é: {nivel}')


x = 3
print(f'Removendo valor {x}...')
ab.remover(x)
print('Exibindo árvore em Ordem')
ab.em_ordem()
print('\nExibindo árvore em Pré Ordem')
ab.pre_ordem()
print('\nExibindo árvore em Pós Ordem')
ab.pos_ordem()
print('')