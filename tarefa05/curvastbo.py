import libsort2022 as ordena
import random
import time

def maiormenor(a, b):
    return a > b

#$ cria uma lista com valores aleatorios de 0 ao tamanho da lista 
def criaLista(tamanhoLista):
    lista = []
    for i in range(tamanhoLista):
        lista.append(random.randint(0,tamanhoLista))
    return lista

#$ ordena uma lista criada com a funcao criaLista usando os metodos bubble, insertion, selection
#$ e printa na tela o tamanho da lista e quantas trocas foram feitas em cada metodo de ordenacao
def main():  
    inicio = time.time()
    arquivo = open('saida.txt','w')
    for i in range(10,5010,10):
        lista = criaLista(i)
        print()
        print(f'{i} {ordena.bubbleSort(lista[:], maiormenor)} {ordena.insertionSort(lista[:], maiormenor)} {ordena.selectionSort(lista[:], maiormenor)}')
        
        linha = f'{i},{ordena.bubbleSort(lista[:], maiormenor)},{ordena.insertionSort(lista[:], maiormenor)},{ordena.selectionSort(lista[:], maiormenor)}\n'
        arquivo.write(linha)
    
    print(f"\n{time.time() - inicio}")
        


if __name__ == '__main__':
    main()