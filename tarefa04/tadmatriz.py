from asyncore import write

#@   Função que cria matrizes
def cria(linhas, colunas):
    #listaLinha sera o numero de item em uma linha
    listaLinha = []
    #lista sera a lista com a quantidade de linhas
    lista = []
    for i in range(int(colunas)):
        listaLinha.append(0)
    for i in range(int(linhas)):
        lista.append(listaLinha[:])    
    return lista


#@   Pega o elemento especificado da matriz
def getElem(matriz, linha, coluna):
    return matriz[int(linha)-1][int(coluna)-1]


#@  Muda o elemento especificado na matriz
def setElem(matriz, linha, coluna, valor):
    matriz[int(linha)-1][int(coluna)-1] = int(valor)
    return matriz


#@  Soma duas matrizes
def soma(matrizA, matrizB):
    if not len(matrizA) == len(matrizB) and not len(matrizA[0]) == len(matrizB[1]):
        return None     
    for i in range(len(matrizA)):
        for j in range(len(matrizA[i])):
            matrizA[i][j] = int(matrizA[i][j]) + int(matrizB[i][j])
    return matrizA


#@  Multiplica todos os valores da matriz pelo valor especificado
def vezesK(matriz, numero):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(matriz[i][j]) * int(numero)
    return matriz


#@  Multiplica duas matrizes
def multi(matrizA, matrizB):
    if len(matrizA[0]) != len(matrizB):
        return None
    matriz = cria(len(matrizA),len(matrizB[0]))
    for c in range(len(matriz)):       
        for a in range(len(matriz[0])):
            for o in range(len(matrizB)):
                matriz[c][a] += (int(matrizA[c][o]) * int(matrizB[o][a]))
    return matriz


#@  Clona a matriz
def clona(matriz):
    return matriz[:]


#@  Pega os valores da diagonal principal
def diagP(matriz):
    if len(matriz) != len(matriz[0]):
        return None
    lista = []
    for i in range(len(matriz)):
        lista.append(matriz[i][i])
    return lista

#@  Pega os valores da diagonal secundária
def diagS(matriz):
    if len(matriz) != len(matriz[0]):
        return None
    lista = []
    a = len(matriz) - 1
    b = 0
    while a >= 0:    
        lista.append(matriz[b][a])
        a -= 1
        b += 1
    return lista


#@  Retorna a quantidade de linhas da matriz
def quantLinhas(matriz):
    return len(matriz)


#@  Retorna a quantidade de colunas da matriz
def quantColunas(matriz):
    return len(matriz[0])


#@  Carrega a matriz de um arquivo
def carregamat(nomeArq):
    arquivo = open(nomeArq,'r')
    linha = arquivo.readline().split()
    lista = []
    while linha != []:
        lista.append(linha)
        linha = arquivo.readline().split()
    return lista


#@  Salva a matriz em um arquivo
def salvamat(matriz, nomeArq):
    arquivo = open(nomeArq,'w')
    linha = ''
    for i in range(len(matriz)):
        for e in range(len(matriz[0])):
            linha += str(matriz[i][e]) + ' '
        arquivo.write(linha.strip())
        arquivo.write('\n')
        linha = ''
    return matriz


#@  Transforma a matriz em string
def tostring(matriz):
    texto = ''
    for i in range(len(matriz)):
        for e in range(len(matriz[0])):
            texto += str(matriz[i][e]) + ' '
        texto += '\n'
    return texto



def transposta(matriz):
    matrix = cria(len(matriz[0]),len(matriz))
    for i in range(len(matriz[0])):
        for e in range(len(matriz)):
            matrix[i][e] = matriz[e][i]
    return matrix