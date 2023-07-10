import numpy as np
import random

caracteres = [None,' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', 
              ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[','\\',
              ']', '^', '_', '`', '{', '|', '}', '~', 'A', 'B', 'C', 'D', 'E', 
              'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 
              'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
              's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç', 'Ç', 'á', 'à', 'ã', 
              'â', 'é', 'è', 'ê', 'í', 'ì', 'î', 'ó', 'ò', 'õ', 'ô', 'ú', 'ù', 
              'û', 'Á', 'À', 'Ã', 'Â', 'É', 'È', 'Ê', 'Í', 'Ì', 'Î', 'Ó', 'Ò', 
              'Õ', 'Ô', 'Ú', 'Ù', 'Û', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#@   Função que cria matrizes
def cria(linhas, colunas):
    listaLinha = []
    lista = []
    for i in range(int(colunas)):
        listaLinha.append(0)
    for i in range(int(linhas)):
        lista.append(listaLinha[:])    
    return lista

#@  Multiplica duas matrizes
def multi(matrizA, matrizB):
   
    matriz = [0,0,0]
    for c in range(len(matriz)):       
            for o in range(len(matrizB)):
                matriz[c] += (matrizA[c][o] * matrizB[o])
    return matriz

#@ cria a string criptografada
def encripta(matriz):
    texto = ''  
    for i in range(len(matriz)):
        texto += str(matriz[i]) + caracteres[random.randint(1, 121)]
    return texto

#@  Transforma a matriz em string
def tostring(matriz):
    texto = ''  
    for i in range(len(matriz)):
        if matriz[i] != None:
            texto += str(matriz[i])
    return texto

#@ recebe um texto e picota em tamanhos iguais
def picota(texto, numero):
  
  if len(texto) < numero:
      numero = len(texto)
  index = 0
  index_sup = numero
  lista = []
  while len(texto) > index:
    aux = texto[index:index_sup]
    lista.append(aux)
    index = index + numero
    index_sup = index_sup + numero
  return lista

#@ Transforma a string em uma matriz
def strinMat(texto, quantlinha, quantcoluna):
    index = 0
    tamtext = len(texto)
    matriz = cria(quantlinha, quantcoluna)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if index < tamtext:
                matriz[i][j] = texto[index]
                index += 1
            else:
                matriz[i][j] = None
    return matriz

#@ Tranforma uma matriz de caracteres em uma matriz de index
def matrizIndex(matriz):
    lista = []
    for i in range(len(matriz)):
        lista.append(caracteres.index(matriz[i]))
    return lista

#@ Tranforma uma matriz de index em uma matriz de caracteres
def traduzCode(matrizA):
    matriz = np.around(matrizA).tolist()
    for i in range(len(matriz)):
        matriz[i] = caracteres[int(matriz[i])]
    return matriz

#@ cria uma matriz com os valores da string criptografada
def picotaCifra(texto, numero):
    lista = []
    vetores = []
    aux = ""
    for i in texto:
        if i.isdigit():
            aux += i        
        elif aux:
            lista.append(int(aux))
            aux = ""
            if len(lista) == numero:
                vetores.append(lista)
                lista = []
    if len(aux) != 0:
        lista.append(int(aux))
        if len(lista) == numero:
            vetores.append(lista)
        else:
            for i in range(numero - len(lista)):
                lista.append(0)
            vetores.append(lista)
    return vetores