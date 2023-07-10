import tadmatriz as tad
import numpy as np
import os

def ler_arquivo(name):
  #, econding="utf-8"
  with open (name, 'r') as arq:
    texto = arq.read()
  return texto #.replace("\n", " ")


def limpa_tela():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")


def save(texto):
  op = int(input('''Deseja salvar a mensagem gerada em um arquivo .txt?
  Digite [1] - Para sim
  Digite [2] - Para não
  Opção: ''' ))

  if op == 1:
    name = input('Qual o nome do arquivo? ')
    name += ".txt"
    with open (name, 'w', ) as arq: 
      arq.write(texto)
    print('Arquivo salvo com sucesso!')
  
  return None


def decrypt_mens(mensagem_criptografada, key_inverse):
  pfv = ""
  god = []
  
  for i in tad.picotaCifra(mensagem_criptografada, 3): 
      god = tad.multi(key_inverse, i)
      god = tad.traduzCode(god)
      pfv += tad.tostring(god)

  return pfv
    

def encrypt_mens(mensagem, key):
  lista_mensagem = []
  matriz_criptografada = []
  mensagem_criptografada = ""
  
  for i in tad.picota(mensagem, 3):
      lista_mensagem = tad.matrizIndex(i)
      matriz_criptografada = tad.multi(key, lista_mensagem)
      mensagem_criptografada += tad.encripta(matriz_criptografada)
  
  return mensagem_criptografada


def main():
  key = [[1, 2, 0], [1, 3, -2], [5, 1, 1]]
  
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
  
  
  
  menu = '''Criptografia por Cifra de Hill:
    Digite [1] - Para criptografar uma mensagem 
    Digite [2] - Para descriptografar uma mensagem 
    Digite [0] - Para sair\n
    Opção: '''
  
  op = int(input(menu))
  while op!=0:
    #limpa tela
    if op == 1:
        mensagem = input("Escreva a mensagem: ")
        mensagem_criptografada = encrypt_mens(mensagem, key)
        limpa_tela()
        print("Critografia: ", mensagem_criptografada, "\n")
        save(mensagem_criptografada)
        limpa_tela()

    elif op == 2:
        name = input("Digite o caminho para a mensagem: ")
        mensagem = ler_arquivo(name)
        mensagem_descriptografada = decrypt_mens(mensagem, key_inverse)
        limpa_tela()
        print("Descritografia: ", mensagem_descriptografada, "\n")
        save(mensagem_descriptografada)
        limpa_tela()
      
    else:
        limpa_tela()
        print("Opção inválida\n")
    
    op = int(input(menu))


if __name__ == "__main__":
  main()