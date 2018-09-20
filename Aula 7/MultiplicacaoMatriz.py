
matrizA = []
matrizB = []

def cria_matriz(matrizA, matrizB):
    m = []
    while matrizA > 0:
#        m.append([0]*j)
        m = [([0] * matrizB) * matrizA]
        matrizA -= 1
    return m


def multiplica_matriz(matrizA, matrizB):
    linhas = len(matrizA)
    colunas = len(matrizB[0])
    if linhas != colunas:
        return None
    c = cria_matriz(linhas, colunas)
    for x in range(linhas):
        for y in range(colunas):
            for r in range(matrizA[0]):
                c[x][y] += matrizA[x][r] * matrizB[r][y]
    return c


def main():

    matrizA = cria_matriz(2, 3)
    matrizB = cria_matriz(3, 2)


main()
print(multiplica_matriz(2, 3))
