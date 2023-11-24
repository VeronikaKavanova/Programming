radky_sloupce = input().split()
radky = int(radky_sloupce[0])
sloupce = int(radky_sloupce[1])
matice = []
for i in range(radky):
    radek = input().split()
    for j in range(len(radek)):
        radek[j] = int(radek[j])
    matice.append(radek)

def najdi_nejmensi_prvek(matice):
    if matice!= []:
        nejmensi = matice[0][0]
        for radek in matice:
            for prvek in radek:
                if prvek < nejmensi:
                    nejmensi = prvek
        return nejmensi

def odecti_prvek(matice,prvek):
    for i in range(len(matice)):
        for j in range(len(matice[i])):
            matice[i][j] -= prvek
        print(*matice[i], sep=" ")

nejmensi = najdi_nejmensi_prvek(matice)
odecti_prvek(matice,nejmensi)