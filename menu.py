import random
from arvore_binaria import Arvore_busca

ab = Arvore_busca()
opcao = 10

print('---------------------------------------')
print('Bem vindo ao gerador de Árvore Binária!')
print('---------------------------------------')
while opcao!=0:
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
    opcao = input('Faça sua escolha: ')

    while not opcao.isnumeric() or opcao < 0 or opcao > 9:
        opcao = input('Mas eu num te passei as opções? Escolhe uma válida irmão!\nDigite uma opção válida: ')

    if opcao == 1:
        i = input('Digite o valor que deseja INSERIR: ')
        while not i.isnumeric():
            i = input('Pelo amor de Deus, digita um número meu filho: ')
        ab.inserir(i)
        print('Valor inserido com sucesso!')

    elif opcao == 2:
        print('Exibindo árvore Em Ordem')
        ab.em_ordem()
        print('\nExibindo árvore em Pré Ordem')
        ab.pre_ordem()
        print('\nExibindo árvore em Pós Ordem\n')
        ab.pos_ordem()

    elif opcao == 3:
        i = input('\nDigite o valor que deseja BUSCAR: ')
        while not i.isnumeric():
            i = input('Pelo amor de Deus, digita um número meu filho: ')
        print(f'Efetuando Busca do valor {i}...')
        v = ab.busca(i)
        if v is None:
            print(f'{i} Não foi encontrado na árvore')
        else:
            print(f'{v.raiz.dado} Encontrado')

    elif opcao == 4:
        print(f'O nó de menor valor é: {ab.minimo()}')
        print(f'O nó de maior valor é: {ab.maximo()}')

    elif opcao == 5:
        print(f'O número total de nós é: {ab.total_nos()}')

    elif opcao == 6:
        print(f'As folhas da Arvore são: ', end='')
        {ab.folhas()}
        print(f'\nO número total de folhas é: {ab.total_folhas()}')

    elif opcao == 7:
        i = input('\nDigite o valor que deseja verificar a ALTURA: ')
        while not i.isnumeric():
            i = input('Pelo amor de Deus, digita um número meu filho: ')
        altura = ab.altura(i)
        if altura is None:
            print(f'O valor {i} não está contido na Árvore')
        else:    
            print(f'A altura do nó é: {altura}')

    elif opcao == 8:
        i = input('\nDigite o valor que deseja verificar o NÍVEL: ')
        while not i.isnumeric():
            i = input('Pelo amor de Deus, digita um número meu filho: ')
        nivel = ab.nivel(i)
        if nivel is None:
            print(f'O valor {i} não está contido na Árvore')
        else:    
            print(f'O nível do nó é: {nivel}')

    elif opcao == 9:
        i = input('\nDigite o valor que deseja REMOVER: ')
        while not i.isnumeric():
            i = input('Pelo amor de Deus, digita um número meu filho: ')
        else:
            print(f'O valor {i} foi removido da Árvore.\nCaso deseje visualizar a Árvore, escolha a opção 2!')

    else:
        print('O programa foi encerrado, fllws...')