import tadmatriz

def extrai(matriz,eixox,eixoy,tamx,tamy):
    lista = tadmatriz.cria(tamx,tamy)
    num = 1
    if eixoy == 0:
        num = 0
    for i in range(eixoy,tamx):
        for j in range(eixox,tamy+num):
            lista[i - eixoy][j - eixox] = matriz[i][j]
    return lista

def insere(matriz,eixox,eixoy,minsere):
    num = 1
    if eixoy == 0:
        num = 0
    for i in range(eixoy,len(minsere)+num):
        for j in range(eixox,len(minsere[0])):
            matriz[i][j] = minsere[i - eixoy][j - eixox]
    return matriz

def deslocaEsq(matriz):
    mat = matriz[:] ## Faz uma cópia da matriz
    for indexLinha in range(len(mat)):
        linha = mat[indexLinha][1:] + [0]
        mat[indexLinha] = linha
    return mat

def deslocaDir(matriz):
    mat = matriz[:] ## Faz uma cópia da matriz
    for indexLinha in range(len(mat)):
        linha = [0] + mat[indexLinha][:-1]
        mat[indexLinha] = linha
    return mat

def rotDir(matriz):
    mat = matriz[:] ## Faz uma cópia da matriz
    for indexLinha in range(len(mat)):
        linha = [mat[indexLinha][-1]] + mat[indexLinha][:-1]
        mat[indexLinha] = linha
    return mat
    
def rotEsq(matriz):
    mat = matriz[:] ## Faz uma cópia da matriz
    for indexLinha in range(len(mat)):
        linha = mat[indexLinha][1:] + [mat[indexLinha][0]]
        mat[indexLinha] = linha
    return mat

def vizinhos(matriz, coluna,linha):
    lista = []
    aux = 0
    loga = 1
    logb = 2
    for i in range(8):
        if i < 3:
            logb -= 1
            lista.append(matriz[linha - loga][coluna - logb])
            aux += 1
        elif i < 5:
            loga -= 1
            lista.append(matriz[linha - loga][coluna - logb])
            aux += 1
        elif i < 7: 
            logb +=1
            lista.append(matriz[linha - loga][coluna - logb])
            aux += 1
        else: 
            loga += 1
            lista.append(matriz[linha - loga][coluna - logb])
    return lista