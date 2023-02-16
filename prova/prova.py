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
    arqout = open('./prova/arqout.txt','w')
    dic_aux = {}
    chave = list(dic.keys())

    for pais in chave:
        for j in dic[pais]:
            corte = j.split('.')
            aux = len(corte)

            # Pega a terceira parte da url (com, org, net)
            if corte[aux-2] in dic_aux:
                dic_aux[corte[aux-2]] += 1
            else:
                dic_aux[corte[aux-2]] = 1
        
        cod_pais = pais + ':' + ' \n'
        arqout.write(cod_pais)
        chave_aux = list(dic_aux.keys())
        
        # Escreve as quantias de cada dominio dos países
        for dominio in chave_aux:
            StrQuantdominio = ' ' + dominio + ': ' + str(dic_aux[dominio]) + '\n'
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