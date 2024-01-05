from collections import deque

def zpracuj_vstup():

    pocet_prekazek = "-"

    while pocet_prekazek == "-":
        radek = input().split()
        if len(radek) != 0:
            pocet_prekazek = int(radek[0])

    souradnice = []
    ukazatel_radku = 1

    while len(souradnice) != 2*pocet_prekazek + 4:
        if ukazatel_radku < len(radek):
            souradnice.append(int(radek[ukazatel_radku]))
            ukazatel_radku += 1
        else:
            radek = input().split()
            ukazatel_radku = 0

    prekazky = []
    for kolikata in range(pocet_prekazek):
        prekazky.append(souradnice[0+2*kolikata : 2+2*kolikata])
    start = souradnice[2*pocet_prekazek : 2*pocet_prekazek+2]
    cil = souradnice[2*pocet_prekazek+2:]

    return prekazky, start, cil

def nejkratsi_cesta(start, cil, prekazky):    
    """najde nejkratší cestu ze startu do cíle pomocí BFS"""

    def vygeneruj_sousedni(policko):
        """ vygeneruje všechny sousední políčka zadaného, na které král může vstoupit """
        sousedni = []
        for i in range(-1,2): 
            for j in range(-1,2):
                if i == 0 and j == 0: #nechceme generovat znova stejné políčko
                    continue
                radek = int(policko[0]) + i
                sloupec = int(policko[1]) + j
                if (radek and sloupec > 0) and (radek and sloupec < 9): #pokud je pole na šachovnici
                    pole = [radek,sloupec]
                    if pole not in prekazky: #a pokud to není překážka
                        sousedni.append(pole) #dá se na něj vstoupit
        return sousedni

    fronta = deque() # do fronty budeme ukládat vždy za sebou políčko a cestu, jak jsme se do něj dostali
    fronta.append(start)
    fronta.append([start])
    navstivena_policka = {} #sem budeme ukládat políčka, na kterých jsme už byli 
    #a kolik kroků nám trvalo se do nich dostat. To 

    while len(fronta) != 0:
        policko = fronta.popleft() #další políčko se uloží sem
        sousedni_policka = vygeneruj_sousedni(policko) #vygenerujeme všechna políčka na která se z další můžeme dostat
        
        for soused in sousedni_policka:
            cesta = list(fronta[0]) #chceme, aby každý soused začal se základní cestou
            if soused not in cesta:
                cesta.append(soused) #tady se cesta upraví, ale další soused si načte tu starou
                if soused == cil:
                    return cesta
                fronta.append(soused)
                fronta.append(cesta)
        fronta.popleft() #chceme se zbavit staré cesty
    return -1

def vytiskni_vystup(cesta):
    if cesta == -1:
        print(-1)
    else:
        for pole in cesta:
            print(*pole, end= " ")

prekazky, start, cil = zpracuj_vstup()
cesta = nejkratsi_cesta(start,cil,prekazky)
vytiskni_vystup(cesta)