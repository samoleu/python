import tadmatriz as tm

# -------------------------------------------------------------------
# Exercicio onde utilizamos os algoritmos presentes no 'tadmatriz.py'
# para multiplicar uma matriz A por outra matriz B, somar a matriz C
# com a matriz D e multiplicar a matriz B com a matriz D
# -------------------------------------------------------------------

def main():
    
    # Carrega as matrizes de um arquivo
    a = tm.carregamat('./ExerciciosTAD/matrizes/A.txt')
    b = tm.carregamat('./ExerciciosTAD/matrizes/B.txt')
    c = tm.carregamat('./ExerciciosTAD/matrizes/C.txt')
    d = tm.carregamat('./ExerciciosTAD/matrizes/D.txt')

    # Faz as operações com as matrizes e as salva em arquivos
    aeb = tm.multi(a,b)
    tm.salvamat(aeb, './ExerciciosTAD/matrizes/AxB.txt')
    soma = tm.soma(c, d)
    tm.salvamat(soma, './ExerciciosTAD/matrizes/CmaisD.txt')
    bed = tm.multi(b,d)
    tm.salvamat(bed, './ExerciciosTAD/matrizes/BxD.txt')
    
    # Carrega as matrizes de um arquivo e as printa
    aa = tm.carregamat("./ExerciciosTAD/matrizes/AxB.txt")
    print(aa)
    bb = tm.carregamat("./ExerciciosTAD/matrizes/CmaisD.txt")
    print(bb)
    cc = tm.carregamat("./ExerciciosTAD/matrizes/BxD.txt")
    print(cc)
    
    # print das matrizes viradas 90 graus
    print(tm.transposta(aa))
    print(tm.transposta(cc))
    print(tm.transposta(bb))

if __name__ == '__main__':
    main()