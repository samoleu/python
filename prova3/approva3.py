import libsort2022 as ordena
import sys
sys.setrecursionlimit(6000)


def carrega(nomeArq):
    arquivo = open(nomeArq, 'r', encoding= 'utf8')
    linha = arquivo.readline()
    lista = []
    while linha != '':
        lista.append(linha.split(';'))
        linha = arquivo.readline()
    arquivo.close()
    return lista

def salva(tabela, nomeArq):
    arquivo = open(nomeArq, 'w', encoding= 'utf8')

    for linha in tabela:
        texto = ''
        for item in linha:
            texto += item 
            if item != linha[-1]:
                texto += ';'
        arquivo.write(texto)
    arquivo.close()
        
    return tabela

def compara(valorA, valorB):

    if valorA[0] != valorB[0]:
        return valorA[0] > valorB[0]
    elif valorA[1] != valorB[1]:
        return valorA[1] < valorB[1]
    elif valorA[2] != valorB[2]:
        return valorA[2] < valorB[2]
    elif valorA[5] != valorB[5]:
        return valorA[5] < valorB[5]
    else:
        return valorA[7] > valorB[7]


def main():

    tabela = carrega('bdprova3.txt')

    listaquickNR = ordena.quicksortNR(tabela[:], 0, len(tabela)-1,compara)

    salva(listaquickNR, 'outnr.txt')

    listaquickR = ordena.quicksortR(tabela[:], 0, len(tabela)-1,compara)

    salva(listaquickR, 'outrr.txt')

    return 0

main()
