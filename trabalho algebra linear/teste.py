import tadmatriz as tad
import numpy as np

key = [[1,1,1],[3,5,4],[3,6,5]] #[[1, 2, 0], [1, 3, -2], [5, 1, 1]]

key_inverse =  np.linalg.inv(np.array(key)).tolist() 

caracteres = [None,' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', 
              ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@','[', '\\',
              ']', '^', '_', '`', '{', '|', '}', '~', 'A', 'B', 'C', 'D', 'E', 
              'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 
              'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
              's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç', 'Ç', 'á', 'à', 'ã', 
              'â', 'é', 'è', 'ê', 'í', 'ì', 'î', 'ó', 'ò', 'õ', 'ô', 'ú', 'ù', 
              'û', 'Á', 'À', 'Ã', 'Â', 'É', 'È', 'Ê', 'Í', 'Ì', 'Î', 'Ó', 'Ò', 
              'Õ', 'Ô', 'Ú', 'Ù', 'Û', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

mensagem = input("mensagem: ")
lista_mensagem = []
matriz_criptografada = []
mensagem_criptografada = ""

for i in tad.picota(mensagem, 3):
   
    lista_mensagem = tad.matrizIndex(i)
    
    matriz_criptografada = tad.multi(key, lista_mensagem)
    print(f"{matriz_criptografada}")
    mensagem_criptografada += tad.encripta(matriz_criptografada)

print(f"\nmensagem cifrada: {mensagem_criptografada}\n")

pfv = ""
god = []

for i in tad.picotaCifra(mensagem_criptografada, 3): 
    god = tad.multi(key_inverse, i)
    god = tad.traduzCode(god)
    pfv += tad.tostring(god)

print(pfv)