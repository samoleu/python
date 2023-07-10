import tadmatriz

def insere(matriz,eixoy,eixox,minsere):
    for i in range(eixoy,len(minsere)+1):
        matriz[i][eixox:eixox+len(minsere[0])] = minsere[i-1][:]

    return matriz

matriz = [[5,4,1,8,3,6],[3,0,5,6,7,4],[9,1,2,8,4,3],[4,5,1,9,0,2],[9,0,7,4,1,3]]
inserida = [[1,1,1],[1,1,1],[1,1,1]]

for i in insere(matriz,1,2,inserida):
    print(i)