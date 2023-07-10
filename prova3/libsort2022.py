def bolha(lst,compara):
    trocou = True

    conttrocas = 0

    while trocou:
        trocou = False
        for i in range(len(lst)-1):
            if compara(lst[i],lst[i+1]):
                lst[i],lst[i+1] = lst[i+1],lst[i]
                trocou = True
                conttrocas += 1
        # for
    # while

    return conttrocas
# fim bolha

def insercao(lst,compara):
    conttrocas = 0

    for i in range(1,len(lst)):
        aux = lst[i]
        j = i - 1
        while (j >= 0) and compara(lst[j],aux):
            lst[j+1] = lst[j]
            j = j - 1
            conttrocas += 1
        # while

        lst[j+1] = aux
    # for i

    return conttrocas
# fim insercao

def selecao(lst,compara):
    conttrocas = 0

    for i in range(len(lst)):
        posmenor = i

        for j in range(i+1,len(lst)):
            if compara(lst[j],lst[posmenor]):
                posmenor = j

        if lst[i] != lst[posmenor]:
            aux = lst[i]
            lst[i] = lst[posmenor]
            lst[posmenor] = aux
            conttrocas += 1

    return conttrocas
# fim selecao

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# CONSTRUA AQUI O QUICKSORT NÃO-RECURSIVO E SUAS FUNÇÕES AUXILIARES, SE HOUVEREM.
def quicksortNR(arr,l,h, compara):
 
    size = h - l + 1
    stack = [0] * (size)
 
    top = -1
 
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
 
    while top >= 0:

        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        p = particao( arr, l, h, compara )
 
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
 
        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
            
    return arr
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@




def quicksortR (lista, inicio, fim, compara ):

    if inicio < fim:
        pos = particao(lista, inicio , fim, compara)
        quicksortR (lista, inicio , pos-1, compara)
        quicksortR (lista, pos+1, fim, compara)
    
    return lista

def particao(lista, inicio , fim, compara ):

    i = inicio +1
    j = fim

    while i <= j:
        while i <= j and compara(lista[i], lista[inicio]):
            i += 1
        while j >= i and not compara(lista[j], lista[inicio]):   
            j-= 1
        if i < j: 
            lista[i], lista[j] = lista[j], lista[i]
    
    lista[inicio], lista[j] = lista[j], lista[inicio]

    return j

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# É PROVÁVEL QUE AS FUNÇÕES AUXILIARES SEJAM AS MESMAS, TANTO PARA O CASO RECURSIVO 
# QUANTO PARA O NÃo-RECURSIVO. 
# SE ESTE FOR O CASO, CRIE APENAS 1 CṔOIA DO CÓDIGO.



















