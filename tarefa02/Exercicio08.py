def processa(dic,linha):
	palavra = ''
	for i in linha:
		if i.isalnum():
			palavra += i
		elif palavra != '':	
			if palavra in dic:
				dic[palavra] += 1
				palavra = ''
			else:
				dic[palavra] = 1
				palavra = ''
	return dic

def main():
	arquivo = open('./tarefa02/biblia-em-txt.txt','r',encoding = "UTF-8")
	linha = arquivo.readline()
	dic = {}
	while linha != '':
		processa(dic,linha)
		linha = arquivo.readline()
	arquivo.close()
	arquivOut = open('./tarefa02/saidadic.txt','w',encoding = "UTF-8")
	organizador = list(dic.values())
	aux = list(dic.keys())
	organizador.sort()

	for i in organizador:
		a = False	
		j = 0
		while a == False:
			if dic[aux[j]] == i:
				arquivOut.write(f'{aux[j]},{dic[aux[j]]}\n')
				a = True
				del aux[j]
				j += 1
			else:
				j += 1
	arquivOut.close()
	
	

main()
