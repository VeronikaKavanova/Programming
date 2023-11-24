def priprav_platno(vstup):    

    platno = []
    for i in range(vstup[-1]):
        radek = []
        for i in range(vstup[-1]):
            radek.append("-")
        platno.append(radek)
    return platno

def tiskni_ctverec(platno, velikost, znamenko):
    for radek in range(velikost):
        for sloupec in range(velikost):
            platno[-1 - radek][-1 - sloupec] = znamenko
    return platno

vstup = input().split()
for i in range(len(vstup)):
    vstup[i] = int(vstup[i])

platno = priprav_platno(vstup)

pocitadlo_znamenka = 1
for ctverec in vstup[-2::-1]:
    if pocitadlo_znamenka == 1:
        znamenko = "+"
    else:
        znamenko = "-"
    platno = tiskni_ctverec(platno,ctverec,znamenko)
    pocitadlo_znamenka *= -1

for i in platno:
    print(*i, sep= "")