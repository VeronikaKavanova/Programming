matice = []
radek = input().split()
matice.append(radek)
n = len(radek)
for i in range(n-1):
    radek = input().split()
    matice.append(radek)

def symetrie(matice):
    
    symetrie_hlavni = 1
    symetrie_vedlejsi = 1
    symetrie_svisla = 1
    n = len(matice)
    for i in range(n):
        for j in range(len(matice[i])):
            x = matice[i][j]
            yhlavni = matice[j][i]
            yvedlejsi = matice[n-1-j][n-1-i]
            ysvisla = matice[i][n-1-j]
            if x != yhlavni:
                symetrie_hlavni = 0
            if x != yvedlejsi:
                symetrie_vedlejsi = 0
            if x != ysvisla:
                symetrie_svisla = 0
    
    return [symetrie_hlavni, symetrie_vedlejsi, symetrie_svisla]

vysledek = symetrie(matice)
for i in vysledek:
    print(i, end = " ")