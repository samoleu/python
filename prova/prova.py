# -------------------------------------------------------------------------
# O programa processa um arquivo (webdomains.txt) que contem urls
# de todo o mundo, ele as separa pelo codigo do pais (br, us, uk, etc)
# e passa os dominio topo de nivel (org, com, net, etc) e a frequência que
# cada um aparece
# -------------------------------------------------------------------------

def processa(arqin):
    palavra = ''
    arqin = open('./prova/webdomains.txt','r')
    linha = arqin.readline().strip('\n')
    dic = {}

    # logica para identificar '.' na linha
    while linha != '':
        cont_ponto = 0
        aux = 0
        for pais in linha:
            if pais == '.':
                cont_ponto += 1
        for pais in linha:
            if aux == cont_ponto:
                palavra += pais
            elif pais == '.':
                aux += 1
    # adiciona o codigo do pais no dicionario
        if palavra in dic:
            dic[palavra].append(linha)
            palavra = ''

        else:
            dic[palavra] = [linha]
            palavra = ''

        linha = arqin.readline().strip('\n')
    arqin.close()
    return dic

def relatorioDomains(arqout,dic):
    
    # arquivo de saida
    arqout = open(arqout,'w')
    lista_aux = []

    for i in range(len(lista_d)):
        for e in range(len(lista_d[i])):
            corte = j.split('.')
            aux = len(corte)

            # Pega a terceira parte da url (com, org, net)
            if corte[aux-2] in lista_aux:
                lista_aux[corte[aux-2]] += 1
            else:
                lista_aux[corte[aux-2]] = 1
        
        cod_pais = pais + ':' + ' \n'
        arqout.write(cod_pais)

        
        # Escreve as quantias de cada dominio dos países
        for dominio in lista_aux:
            StrQuantdominio = ' ' + dominio + ': ' + str(lista_aux[dominio]) + '\n'
            arqout.write(StrQuantdominio)
        arqout.write("\n")
    arqout.close()
    return dic

def main():
    arqin = 0
    arqout = 0

    dic = processa(arqin)
    relatorioDomains(arqout,dic)

if __name__ == '__main__':
    main()