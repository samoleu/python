# ------------------------------------------------------------------
# Este programa proposto pelo professor conta quantas palavras tem
# em determinado arquivo .txt que no caso teste foi usado a biblia
# ------------------------------------------------------------------


# A função processa identifica as palavras, identificando o que não é letra 
# ou número e adicionando-a com valor 1 ou iterando na variavel 'palavras'.
# A função recebe um dicionário e uma string (uma linha do arquivo) 
# Não retorna nada, só processa os dados  
def processa(palavras,linha):
	palavra = ''
	for i in linha:	
		if i.isalnum():
			palavra += i
		elif palavra in palavras:
			palavras[palavra] += 1
			palavra = ''
		elif palavra != '':
			palavras[palavra] = 1
			palavra = ''

def main():

	# abertura do arquivo que será usado para contar as palavras
	arquivo = open('./Conta Palavras/biblia-em-txt.txt','r',encoding = "UTF-8")
	linha = arquivo.readline()

	# dicionario que terá as palavras como key e a quantidade como value 
	palavras = {}
	
	# chama a função processa até 'linha' estar vazia, o que significa 
	# que o arquivo foi lido inteiro
	while linha != '':
		processa(palavras,linha)
		linha = arquivo.readline()
	arquivo.close()
	
	# abertura do arquivo de saída, onde terá os dados da quantidade de palavras 
	# ordenadas do maior para o menor
	arquivOut = open('./Conta Palavras/saidadicEx2.txt','w',encoding = "UTF-8")
	
	# variavel auxiliar para listar os valores do dicionario 
	# e ordenados do menor para o maior em uma lista
	organizador = list(palavras.values())
	organizador.sort(reverse=True)
	
	# variavel auxiliar para listar as chaves do dicionario
	aux = list(palavras.keys())
	
	# laço de repetição usado para inserir os dados no arquivo de saida
	j = 0
	while j <= len(organizador):
		for i in aux:
			if palavras[i] == organizador[j]:
				arquivOut.write(f'{i} : {palavras[i]}\n')
				aux.remove(i)
				break
		j += 1
	arquivOut.close()

if __name__ == '__main__':
	main()