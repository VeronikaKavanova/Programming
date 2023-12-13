# pocet dnu mezi dvema daty

def JePrestupnyRok(r):
    if r % 4 == 0 and (r%100 != 0 or r%400 == 0):
        return True
    else:
        return False

def CisloDne(d,m,r):
    M = [0, 31,28,31,30,31,30, 31,31, 30,31,30,31]
    for i in range(1,13):
        M[i] += M[i-1]
    if JePrestupnyRok(r) and m >2:
        d += 1
    #return int((r-1)*365.2425) + M[m-1] + d
    return (r-1)*365 + (r-1)//4 - (r-1)//100 + (r-1)//400 + M[m-1] + d


def PocetDnu( d1, m1, r1, d2, m2, r2):
    return CisloDne(d2,m2,r2) - CisloDne(d1,m1,r1)

def OtestujPocetDnu(vstup, spravny_vystup):
    global pocet_testu
    global pocet_chyb

    pocet_testu += 1
    print(".", end="" )

    vys = PocetDnu(*vstup)
    if vys != spravny_vystup:
        pocet_chyb += 1
        print(f"CHYBA: {vstup} -> {vys} misto {spravny_vystup}")