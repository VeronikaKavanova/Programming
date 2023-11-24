les = []

vstup = input().split()
while vstup != []:
    for i in range(len(vstup)):
        vstup[i] = int(vstup[i])
    les.append(vstup)
    vstup = input().split()

def velikost_platna(les):
    sloupcu = 1 + 2*(les[0][2]-1)
    nejpravejsi = les[0][0] + sloupcu
    nejspodnejsi = les[0][1] + les[0][2] + les[0][3]
    for strom in les:
        sloupcu = 1 + 2*(strom[2]-1)
        vpravo = strom[0] + sloupcu
        if vpravo > nejpravejsi:
            nejpravejsi = vpravo
        dole = strom[1] + strom[2] + strom[3]
        if dole > nejspodnejsi:
            nejspodnejsi = dole
    return nejpravejsi, nejspodnejsi

def platno(sloupcu, radku):
    platno = []
    for i in range(radku):
        radek = sloupcu*["."]
        platno.append(radek)
    return platno

sirka_vyska = velikost_platna(les)
platno = platno(sirka_vyska[0],sirka_vyska[1])

def tiskni_strom(platno, strom):

    x = strom[0]
    y = strom[1]
    k = strom[2]
    l = strom[3]
    
    sloupcu = 1 + 2*(k-1)

    def tiskni_ker():
        hvezd = 1
        for i in range(k):
            radek = platno[y+i] 
            tecek = (sloupcu-hvezd)//2
            for j in range(hvezd):
                radek[x+tecek+j] = "*"
            hvezd += 2
            platno[y+i] = radek

    def tiskni_kmen():
        tecek = (sloupcu-1)//2
        for i in range(l):
            radek = platno[y+k+i]
            radek[x+tecek] = "*"
            platno[y+k+i] = radek    
    
    tiskni_ker()
    tiskni_kmen()

for strom in les:
    tiskni_strom(platno, strom)

for i in platno:
    print(*i, sep= "")