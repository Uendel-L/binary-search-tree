import random
from arvore_binaria import Arvore_busca

ab = Arvore_busca()
opcao = 10

def try_except(string):
    try: 
        opcao = int(input(string))
    except ValueError as err: 
        print('Apenas números são válidos!')
    else: 
        return opcao
    return try_except(string)
    #"Digite a opção que deseja: "

print('---------------------------------------')
print('Bem vindo ao gerador de Árvore Binária!')
print('---------------------------------------')
while True:
    print('''Por favor, Digite uma opção para prosseguirmos:\n
    Para INSERIR, digite 1\n
    Para VISUALIZAR A Árvore, digite 2\n
    Para BUSCAR UM VALOR, digite 3\n
    Para VERIFICAR O MENOR e MAIOR NÓ, digite 4\n
    Para VERIFICAR O TOTAL DE NÓS, digite 5\n
    Para VERIFICAR AS FOLHAS, digite 6\n
    Para VERFICAR A ALTURA DE UM NÓ, digite 7\n
    Para VERIFICAR O NÍVEL DE UM NÓ, digite 8\n
    Para REMOVER UM NÓ, digite 9\n
    Para SAIR, digite 0''')
    print('---------------------------------------')
    opcao = try_except('Digite a opção que deseja: ')

    if opcao == 1:
        i = try_except('Digite o valor que deseja INSERIR: ')
        ab.inserir(i)
        print('Valor inserido com sucesso!')

    elif opcao == 2:
        if ab.raiz==None:
            print('A árvore está vazia.')
        else:
            print('\nExibindo a raíz da árvore')
            print(ab.raiz)
            print('Exibindo árvore Em Ordem')
            ab.em_ordem()
            print('\nExibindo árvore em Pré Ordem')
            ab.pre_ordem()
            print('\nExibindo árvore em Pós Ordem')
            ab.pos_ordem()
            print('')

    elif opcao == 3:
        i = try_except('\nDigite o valor que deseja BUSCAR: ')
        print(f'Efetuando Busca do valor {i}...')
        v = ab.busca(i)
        if v is None:
            print(f'{i} Não foi encontrado na árvore')
        else:
            print(f'{v.raiz.dado} Encontrado')

    elif opcao == 4:
        if ab.raiz==None:
            print('A árvore está vazia.')
        else:
            print(f'O nó de menor valor é: {ab.minimo()}')
            print(f'O nó de maior valor é: {ab.maximo()}')

    elif opcao == 5:
        if ab.raiz==None:
            print('A árvore está vazia.')
        else:
            print(f'O número total de nós é: {ab.total_nos()}')

    elif opcao == 6:
        if ab.raiz==None:
            print('A árvore está vazia.')
        else:
            print(f'As folhas da Arvore são: ', end='')
            {ab.folhas()}
            print(f'\nO número total de folhas é: {ab.total_folhas()}')

    elif opcao == 7:
        i = try_except('\nDigite o valor que deseja verificar a ALTURA: ')
        altura = ab.altura(i)
        if altura is None:
            print(f'O valor {i} não está contido na Árvore')
        else:    
            print(f'A altura do nó é: {altura}')

    elif opcao == 8:
        i = try_except('\nDigite o valor que deseja verificar o NÍVEL: ')
        nivel = ab.nivel(i)
        if nivel is None:
            print(f'O valor {i} não está contido na Árvore')
        else:    
            print(f'O nível do nó é: {nivel}')

    elif opcao == 9:
        i = try_except('\nDigite o valor que deseja REMOVER: ')
        print(i)
        ab.remover(i)
        print(f'O valor {i} foi removido da Árvore.\nCaso deseje visualizar a Árvore, escolha a opção 2!')
    
    elif opcao==0:
        print('O programa foi encerrado, fllws...')
        break

    else:
        opcao = input('Mas eu num te passei as opções? Escolhe uma válida irmão!\nDigite uma opção válida: ')