import tadmatriz

def vizinhos(matriz,linha,coluna):
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

matriz = [[5,4,1,8,3,6],[3,0,5,6,7,4],[9,1,2,8,4,3],[4,5,1,9,0,2],[9,0,7,4,1,3]]

print(vizinhos(matriz,1,2))