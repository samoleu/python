def processa(dic,texto):
	cont = 0
	palavra = ""
	for i in texto:
		if i.isalnum():
			cont += 1
			palavra += i
		elif palavra != '':			
			if cont in dic:
				dic[cont].append(palavra)
				
			else:
				dic[cont] = [palavra]
			cont = 0
			palavra = ""
	return dic	

def main():
	arquivo = open("./tarefa01/biblia-em-txt.txt",'r', encoding = "UTF-8")
	dic = {}
	frase = arquivo.readline()
	while frase != '':			
		processa(dic,frase)
		frase = arquivo.readline()
	arquivo.close()
	
	arquivoSaida = open("./tarefa01/saidadic.txt",'w', encoding= 'UTF-8')
	lista = []
	for i in dic.keys():
		lista.append(i)
	lista.sort()
	for i in lista:
		palavra = str('{0}:{1}\n\n'.format(i,dic[i]))
		arquivoSaida.write(palavra)
	arquivoSaida.close()
	
main()