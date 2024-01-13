from collections import deque

def zpracuj_vstup():
    pocet_mest = int(input())
    pocet_cest = int(input())
    if pocet_mest == 1:
        return False #pokud máme jen jedno město, nebudou žádné cesty a tudíž hlavní jádro algoritmu nebude fungovat
    seznam_cest = deque()
    for i in range(pocet_cest):
        cesta = input().split()
        for i in range(2):
            cesta[i] = int(cesta[i])
        seznam_cest.append(cesta)
    return seznam_cest

def roztrid(cesty):
    """roztřídí města do dvou skupin, tak aby spolu s cestami tvořili bipartitní graf"""
    #dvě skupiny do kterých budeme rozdělovat města, používáme množiny, abychom neměli duplikáty měst
    A = set()
    B = set()

    while len(cesty) != 0: #procházíme všechny cesty a roztřizujeme města do skupin
        cesta = cesty.popleft()
        if (cesta[0] in A and cesta[1] in A) or (cesta[0] in B and cesta[1] in B): #pokud jsou obě města v jedné skupině:
            return False #podmínka byla porušena
        elif cesta[0] in A: #druhé město už v B buď je nebo tam být musí
            B.add(cesta[1])
        elif cesta[0] in B:
            A.add(cesta[1])
        else:
            #pokud první město ještě není nikde, zjistíme, kam musí patřit podle druhého
            if cesta[1] in A:
                B.add(cesta[0])
            elif cesta[1] in B:
                A.add(cesta[0])
            else:
                #pokud ani jedno ještě není umístěno
                if len(cesta) == 2: #tzn. ještě nebyla označena jako bezproblémová, chceme si ji nechat nakonec
                    cesta.append("bezproblemova") #označíme si, že už jsme ji jednou viděli
                    cesty.append(cesta) #a vrátíme ji nakonec
                else: #už jsme ji viděli, tj. ve frontě nám zbývají samé cesty, kterým je zatím jedno, kam které město umístíme
                    A.add(cesta[0])
                    B.add(cesta[1])
                    #to teď možná ovlivní ostatní cesty, proto tuto kontrolu děláme až nakonec, jestli je to opravdu stále jedno

    return A, B
            
cesty = zpracuj_vstup()
if cesty == False: #tzn. nedostali jsme cesty, ale znak, že máme jen jedno město
    print(1)
else:
    vysledek = roztrid(cesty)
    if vysledek == False:
        print("Nelze")
    else:
        A, B = list(vysledek[0]), list(vysledek[1])
        A.sort()
        B.sort()
        if A[0] < B[0]:
            print(*A)
            print(*B)
        else:
            print(*B)
            print(*A)