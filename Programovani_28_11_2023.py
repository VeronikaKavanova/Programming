print([x*x for x in range(11)])
print([(x,y) for x in range(11) for y in range(11)])

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

pocet_chyb = 0
pocet_testu = 0

OtestujPocetDnu((28,11,2023, 29,11,2023),1)
OtestujPocetDnu((29,11,2023, 28,11,2023),-1)
OtestujPocetDnu((29,11,2023, 29,11,2023),0)
OtestujPocetDnu((28,11,2023, 30,11,2023),2)
OtestujPocetDnu((30,11,2023, 28,11,2023),-2)
OtestujPocetDnu((1,1,2023, 1,2,2023),31)
OtestujPocetDnu((31,12,1999, 1,1,2000),1)
OtestujPocetDnu((31,12,1998, 1,1,1999),1)
OtestujPocetDnu((31,12,2000, 1,1,2001),1)
OtestujPocetDnu((31,12,2000, 1,1,2002),366)
OtestujPocetDnu((28,2,2002, 1,3,2002),1)
OtestujPocetDnu((28,2,2004, 1,3,2004),2)
OtestujPocetDnu((28,2,1900, 1,3,1900),1)
OtestujPocetDnu((1,1,2000, 1,1,2001),366)
OtestujPocetDnu((1,1,2001, 1,1,2002),365)
OtestujPocetDnu((1,1,2000, 1,1,2000),0)

OtestujPocetDnu((1,1,2000, 31,12,1999),-1)

OtestujPocetDnu((1,1,2000, 1,1,2010),3653)


print(f"Chyby/Testy: {pocet_chyb}/{pocet_testu}")

#program vytiskne celociselny podil dvou cisel zadanych na vstupu

kOK = 0
kDELENI_NULOU = 7000001 #vybrat si číslo, které nás překvapí. Které nečekáme
kNENI_CISLO = 7000002
kSPATNY_POCET_OPERANDU = 7000003

def Podil(vstup):
    vv = vstup.split()
    if len(vv) != 2:
        return (kSPATNY_POCET_OPERANDU,0)
    try:
        a = int(vv[0])
        b = int(vv[1])
    except ValueError:
        return (kNENI_CISLO, 0)
    if b == 0:
        return (kDELENI_NULOU, 0)
    return (kOK, a//b)

#vstup = input()
#rozdeleny_vstup = vstup.split()
#print(int(rozdeleny_vstup[0]) // int(rozdeleny_vstup[1]))

def OtestujPodil(vstup, vystup):
    global pocetTestu
    global pocetChyb
    
    pocetTestu += 1
    vys = Podil(vstup)
    if vys != vystup:
        pocetChyb += 1
        print(f"CHYBA: {vstup} -> {vys} misto {vystup}")

pocetTestu = 0
pocetChyb = 0

OtestujPodil("4 2", (kOK,2))
OtestujPodil("15 3",(kOK,5))
OtestujPodil("15 4",(kOK,3))
OtestujPodil("15 0",(kDELENI_NULOU,0))
OtestujPodil("nejake slovo",(kNENI_CISLO,0))
OtestujPodil("1",(kSPATNY_POCET_OPERANDU,0))
OtestujPodil(" 1",(kSPATNY_POCET_OPERANDU,0))
OtestujPodil("1 ",(kSPATNY_POCET_OPERANDU,0))
OtestujPodil("1 2 3",(kSPATNY_POCET_OPERANDU,0))
OtestujPodil("a 2 3",(kSPATNY_POCET_OPERANDU,0))
OtestujPodil("1 2 3 4 5 6 7 8 9 0",(kSPATNY_POCET_OPERANDU,0))


print(f"Chyby/Testy: {pocetChyb}/{pocetTestu}")

assert 1<2, "Něco není v pořádku"

"""
CHYBA = - 777

def NactiCislo():
    try:
        x = int(input())
    except ValueError:
        return CHYBA
    return x
"""

"""
def Pocitej():
    try:
        # ...
        a = NactiCislo()
    except NejakaJinaVyjimka:
        # ... 
"""
"""
while True:
    try:
        x = int(input("Zadej číslo: "))
        break
    except ValueError:
        print("Zkus to znovu.")
"""
a: int = 5
b: str = "abc"
a = "xyz"
b = a
print(a,b)