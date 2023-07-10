import tadmatriz

def extrai(matriz,eixoy,eixox,tamx,tamy):
    lista = tadmatriz.cria(tamx,tamy)
    for i in range(eixoy,tamx+1):
        lista[i-eixoy][:] = matriz[i][eixox:eixox+tamx]
        
    return lista

matriz = [[5,4,1,8,3,6],[3,0,5,6,7,4],[9,1,2,8,4,3],[4,5,1,9,0,2],[9,0,7,4,1,3]]
print(extrai(matriz,1,2,3,3))