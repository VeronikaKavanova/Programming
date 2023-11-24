class ctecka:
    def __init__(self):
        self.zbytek = []
    
    def PrectiCislo(self):
        return int(self.PrectiSlovo())

    def PrectiSlovo(self):
        while self.zbytek == []:
            self.zbytek = input().split()
        return self.zbytek.pop(0)

class tiskarna:
    def __init__(self, sirka):
        self.sirka = sirka
        self.kolikUzJsemVytisklaZnaku = 0
    def vytiskni_slovo(self, slovo):
        if self.kolikUzJsemVytisklaZnaku == 0:
            print(slovo, end= " ")
            self.kolikUzJsemVytisklaZnaku = len(slovo) + 1
        elif self.kolikUzJsemVytisklaZnaku + len(slovo) > self.sirka:
            print()
            print(slovo, end= " ")
            self.kolikUzJsemVytisklaZnaku = len(slovo) + 1
        else:
            print(slovo, end = " ")
            self.kolikUzJsemVytisklaZnaku += len(slovo) + 1


ctecka = ctecka()
tiskarna = tiskarna(30)
slovo = ctecka.PrectiSlovo()
while slovo != ".":
    tiskarna.vytiskni_slovo(slovo)
    slovo = ctecka.PrectiSlovo()

slovo = ctecka.PrectiSlovo()
while slovo != ".":
    print(slovo)
    slovo = ctecka.PrectiSlovo()
ctecka.zbytek = []

soucet = 0
x = ctecka.PrectiCislo()
while x != -1:
    soucet += x
    x = ctecka.PrectiCislo()
print(f"Soucet: {soucet}")



class Komplex:
    def __init__(self, re=0, im=0): #pokud to nebude zadáno, bude to 0, může se to dělat i u funkcí
        self.Re = re
        self.Im = im
    def abs(self):
        return(self.Re**2+self.Im**2)**(1/2)

k = Komplex(3,4)
k2 = Komplex()
print(k.abs(),k2.abs()) # bez parametru

#program čte ze vstupu slova tiskne je do řádek, které nebudou delší než 30 znaků
#čtečka a tiskárna
"""
slovo = ctecka.precti_slovo()
while slovo != "":
    tiskarna.vytiskni(slovo)
    slovo = ctecka.precti_slovo()
tiskarna.konec()
"""

a,b,c = 1,2,3
print(a,b,c)

a,b = b,a
print(a,b,c)

d = {"jablko":"apple"}
print(d["jablko"])
d["pomeranc"] = "orange"
d["dvacet"] = 20
print(d)

#vypiš 20 nejčastějších slov, ze seznamu ukončeného slovem konec
N = 50
KONEC = "END"

DATA = """
a,b,c = 1,2,3
print(a,b,c)

a,b = b,a
print(a,b,c)

d = {"jablko":"apple"}
print(d["jablko"])
d["pomeranc"] = "orange"
d["dvacet"] = 20
print(d)

#vypiš 20 nejčastějších slov, ze seznamu ukončeného slovem konec
N = 50
KONEC = "END"

zbytek = None
def PrectiSlovo():
    global zbytek
    if zbytek == None:
        zbytek = DATA.split()
    if zbytek == []:
        return KONEC
    else:
        slovo = zbytek.pop(-1) #vezme daný prvek, vymaže ho a vrátí ho 
        #zbytek.pop(0) kvadratická složitost, 1 vezme první, N slov posune, aby zaplnil indexy. -1 je lineární složitost
        if slovo[-1] in ".,?!": # počet slov * N
            slovo = slovo[:-1]
        return slovo

slova = {}

def PridejSlovo(slovo):
    if slovo in slova:
        slova[slovo] += 1
    else:
        slova[slovo] = 1


def VratNNejcastejsichSlov(N):

    if N > len(slova):
        N = len(slova)

    def VratMiAZnicJednoNejcastejsiSlovo():
        nejpocet = -1
        for slovo in slova:
            if slova[slovo] > nejpocet:
                nejpocet = slova[slovo]
                nejslovo = slovo
        slova[nejslovo] = -1
        return [nejpocet, nejslovo]

    vys = []
    for i in range(N):
        vys.append(VratMiAZnicJednoNejcastejsiSlovo())
    
    return vys

slovo = PrectiSlovo()
while slovo != KONEC:
    if slovo != slovo.upper():    
        PridejSlovo(slovo.lower())
        slovo = PrectiSlovo()

print(*VratNNejcastejsichSlov(N), sep="\n")
END
"""

zbytek = None
def PrectiSlovo():
    global zbytek
    if zbytek == None:
        zbytek = DATA.split()
    if zbytek == []:
        return KONEC
    else:
        slovo = zbytek.pop(-1) #vezme daný prvek, vymaže ho a vrátí ho 
        #zbytek.pop(0) kvadratická složitost, 1 vezme první, N slov posune, aby zaplnil indexy. -1 je lineární složitost
        if slovo[-1] in ".,?!": # počet slov * N
            slovo = slovo[:-1]
        return slovo
"""
slovo = PrectiSlovo()
while slovo != KONEC:
    print(slovo, end = "-")
    slovo = PrectiSlovo()
"""

slova = {}

def PridejSlovo(slovo):
    if slovo in slova:
        slova[slovo] += 1
    else:
        slova[slovo] = 1

"""
PridejSlovo("a")
PridejSlovo("a")
PridejSlovo("a")
PridejSlovo("a")
PridejSlovo("b")
PridejSlovo("C")
PridejSlovo("C")
print(slova)
print(pocty)
"""

def VratNNejcastejsichSlov(N):

    if N > len(slova):
        N = len(slova)

    def VratMiAZnicJednoNejcastejsiSlovo():
        nejpocet = -1
        for slovo in slova:
            if slova[slovo] > nejpocet:
                nejpocet = slova[slovo]
                nejslovo = slovo
        slova[nejslovo] = -1
        return [nejpocet, nejslovo]

    vys = []
    for i in range(N):
        vys.append(VratMiAZnicJednoNejcastejsiSlovo())
    
    return vys

slovo = PrectiSlovo()
while slovo != KONEC:
    if slovo != slovo.upper():    
        PridejSlovo(slovo.lower())
        slovo = PrectiSlovo()

print(*VratNNejcastejsichSlov(N), sep="\n")