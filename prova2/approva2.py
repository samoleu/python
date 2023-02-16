import tadmatriz as tad

def conv(matA, matK):
    
    #@carrega os arquivos
    arqA = tad.carregamat(matA)
    arqK = tad.carregamat(matK)
    
    #@conta a quantidade de linhas
    quantLinhaA = tad.quantLinhas(arqA)
    quantLinhaK = tad.quantLinhas(arqK)
    quantColunaA = tad.quantColunas(arqA)
    quantColunaK = tad.quantColunas(arqK)
    
    #@conta as linhas, colunas e cria a matriz retornada
    colunasMatSaida= quantColunaA - quantColunaK + 1
    linhasMatSaida = quantLinhaA - quantLinhaK + 1
    matriz = tad.cria(linhasMatSaida, colunasMatSaida)
    
    #@processamento da matriz
    for indexLinha_MatrizA in range(linhasMatSaida):
        for indexColuna_MatrizA in range(colunasMatSaida):
            for indexLinha_MatrizK in range(quantLinhaK):
                for indexColuna_MatrizK in range(quantColunaK):
                    
                    ##posicao do item na matriz A que é delimitado pela Matriz K
                    posicaoLinha_MatrizA = indexLinha_MatrizK + indexLinha_MatrizA
                    posicaoColuna_MatrizA = indexColuna_MatrizK + indexColuna_MatrizA

                    ##elementos das matrizes A e K
                    elem_A = int(arqA[posicaoLinha_MatrizA][posicaoColuna_MatrizA])
                    elem_K = int(arqK[indexLinha_MatrizK][indexColuna_MatrizK])
                    matriz[indexLinha_MatrizA][indexColuna_MatrizA] += elem_A * elem_K
    return matriz

def main():
    
    #@chama a função conv e depois salva para os arquivos pré-
    tad.salvamat(conv('./prova2/arquivos/B.txt','./prova2/arquivos/KB.txt'),'./prova2/arquivos/BKB.txt')
    tad.salvamat(conv('./prova2/arquivos/C.txt','./prova2/arquivos/KC.txt'),'./prova2/arquivos/CKC.txt')
    tad.salvamat(conv('./prova2/arquivos/D.txt','./prova2/arquivos/KD.txt'),'./prova2/arquivos/DKD.txt')
    print("fim")
    
if __name__ == '__main__':
    main()