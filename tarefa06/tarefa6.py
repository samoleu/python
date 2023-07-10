import libsort2022 as libsort

def comparaCresce(num1, num2):
    return num1 > num2

def comparaDecresce(num1, num2):
    return num1 < num2


def main():

    lista = []
    linha = open('./tarefa06/bdcepsruas2.txt','r', encoding="utf-8")
    linha.readline().split(',')

    while linha != '':
        lista.append(linha.readline().split(','))
        

    libsort.insertionSort(lista, comparaCresce())

    
    return 0

if __name__ == '__main__':
    main()