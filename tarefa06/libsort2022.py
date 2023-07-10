def bubbleSort(lista, compara): #@ Compara recebe uma função
    cont = 0  
    tamanhoLista = len(lista)
    for i in range(tamanhoLista):
        for j in range(0, tamanhoLista - i - 1):
            if compara(lista[j + 1], lista[j]):
                (lista[j], lista[j + 1]) = (lista[j + 1], lista[j])
                cont += 1                
    return cont


def insertionSort(lista, compara): #@ Compara recebe uma função
    cont = 0  
    cont = 0
    for i in range(1,len(lista)):
        for j in range(i):
            if compara(lista[i], lista[j]):
                lista[j],lista[j+1:i+1] = lista[i],lista[j:i]
                cont += 1
    return cont

def selectionSort(lista, compara): #@ Compara recebe uma função
    cont = 0  
    cont = 0
    for i in range(len(lista)):
        menor = i
        for j in range(i + 1, len(lista)):
            if compara(lista[j], lista[menor]):
                menor = j
        (lista[i], lista[menor]) = (lista[menor], lista[i])
        cont += 1
    return cont