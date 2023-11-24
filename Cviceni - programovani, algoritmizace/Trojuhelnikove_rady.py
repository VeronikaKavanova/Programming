velikost = int(input())
barva_ctverce = input()
barva_radky = input()
barvy = []
while barva_radky != "":
    barva_radky = list(barva_radky)
#    for i in range(2):
#        del barva_radky[-1]
    barvy.append(barva_radky)
    barva_radky = input()

def nakresli_platno(barvy, velikost_ctverce, barva_ctverce):
    platno = []
    for radek in barvy:
        for i in range(velikost):
            platno.append([barva_ctverce]*velikost*len(radek))
    return platno

def nakresli_trojuhelniky(platno,velikost,barvy):
    # radek_barev je několik barev čtverců na jednom řádku
    for index_radku in range(len(barvy)): 
        radek_barev = barvy[index_radku]
        #index_radku nám říká kolikátou řadu momentálně kreslíme
        for index_barvy in range(len(radek_barev)):
            #barva je barva jednoho čtverce
            barva = radek_barev[index_barvy]
            #kolikátý čtverec na této řádce kreslíme
            for radek_ctverce in range(velikost):
                #kolikátý řádek toho čtverce kreslíme
                for sloupec in range(radek_ctverce, velikost):
                    #kolikátý sloupec jednoho čtverce kreslíme
                    platno[index_radku*velikost + radek_ctverce][index_barvy*velikost + sloupec] = barva
    return platno

platno = nakresli_platno(barvy,velikost,barva_ctverce)
platno = nakresli_trojuhelniky(platno,velikost,barvy)
for i in platno:
    print(*i, sep= "")