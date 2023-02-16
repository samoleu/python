import binarytree as bt

def criaArvore(altura, perfeita):


    if altura < 10 or altura > 0:
        if perfeita != 1 or perfeita != 0:
            if perfeita == 1:
                return bt.bst(altura, True)
            else:
                return bt.bst(altura, False)
    else: 
        print('ERRO!!! Altura inválida.')
        return None

def listaInorder(arvore):
    lista = []
    for i in arvore.inorder:
        lista.append(i.value)
    return lista

def listaPreorder(arvore):
    lista = []
    for i in arvore.preorder:
        lista.append(i.value)
    return lista

def listaPostorder(arvore):
    lista = []
    for i in arvore.postorder:
        lista.append(i.value)
    return lista

def listaFolhas(arvore):
    lista = []
    for i in arvore.leaves:
        lista.append(i.value)
    lista.sort()
    return lista

def profundidade(arvore):
    return arvore.height

def subarvore(arvore):
    return [arvore.left, arvore.right]

def busca(arvore, valorBuscado):

    existenode = subarvore(arvore)

    if valorBuscado == arvore.value:
        return True
        
    elif valorBuscado < arvore.value and existenode[0] != None:
        return busca(arvore.left, valorBuscado)
    elif valorBuscado > arvore.value and existenode[1] != None:
        return busca(arvore.right, valorBuscado)
    else:
        return False

arvore = None
escolha = None

while escolha != '':
    
    print()
    print('''Escolha o que deseja fazer:
    [1] Criar árvore binária de busca
    [2] Buscar na árvore
    [3] Percurso em Pré ordem
    [4] Percurso em In ordem
    [5] Percurso em Pós ordem
    [6] Todas as folhas da árvore
    [7] Profundidade da árvore''')
    escolha = input()
    
    if escolha == '1':
        arvore = criaArvore(int(input('qual a altura da árvore [0 a 9]: ')), int(input('\ndeseja uma arvore cheia?\ndigite 0 para não e 1 para sim: ')))
        print(arvore)
    if arvore != None:
        if escolha == '2':
            if busca(arvore, int(input('valor buscado: '))):
                print("\nvalor foi encontrado!!!")
            else:
                print('\nvalor não foi encontrado!!!')
        elif escolha == '3':
            print('\nPré-ordem: ', end= '')
            for i in listaPreorder(arvore):
                print(i, end=' ')
            print()
        elif escolha == '4':
            print('\nIn-ordem: ', end= '')
            for i in listaInorder(arvore):
                print(i, end=' ')
            print()
        elif escolha == '5':
            print('\nPós-ordem: ', end= '')
            for i in listaPostorder(arvore):
                print(i, end=' ')
            print()
        elif escolha == '6':
            print('\nAs folhas da árvore são ', end= '')
            for i in listaFolhas(arvore):
                print(i, end=' ')
            print()
        elif escolha == '7':
            print()
            print('A profundidade da árvore é', profundidade(arvore))
            print()