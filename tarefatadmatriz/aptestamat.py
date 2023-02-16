from this import d
import tadmatriz as tm
def main():
    a = tm.carregamat('./tarefatadmatriz/arquivos texto/A.txt')
    b = tm.carregamat('./tarefatadmatriz/arquivos texto/B.txt')
    c = tm.carregamat('./tarefatadmatriz/arquivos texto/C.txt')
    d = tm.carregamat('./tarefatadmatriz/arquivos texto/D.txt')
    
    
    aeb = tm.multi(a,b)
    tm.salvamat(aeb, './tarefatadmatriz/arquivos texto/AxB.txt')
    soma = tm.soma(c, d)
    tm.salvamat(soma, './tarefatadmatriz/arquivos texto/CmaisD.txt')
    bed = tm.multi(a,b)
    tm.salvamat(bed, './tarefatadmatriz/arquivos texto/BxD.txt')
    aa = tm.carregamat("./tarefatadmatriz/arquivos texto/AxB.txt")
    print(aa)
    bb = tm.carregamat("./tarefatadmatriz/arquivos texto/CmaisD.txt")
    print(bb) 
    cc = tm.carregamat("./tarefatadmatriz/arquivos texto/BxD.txt")
    print(cc)
    print(tm.transposta(aa))
    print(tm.transposta(cc))
    print(tm.transposta(bb))
    


main()