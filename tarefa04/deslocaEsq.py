import tadmatriz

def deslocaEsq(matriz):
    mat = matriz[:] ## Faz uma cópia da matriz
    for indexLinha in range(len(mat)):
        linha = mat[indexLinha][1:] + [0]
        mat[indexLinha] = linha
    return mat

matriz = [[5,4,1,8,3,6],[3,0,5,6,7,4],[9,1,2,8,4,3],[4,5,1,9,0,2],[9,0,7,4,1,3]]

for i in deslocaEsq(matriz):
    print(i)
