#vypiš 20 nejčastějších slov, ze seznamu ukončeného slovem konec
N = 50
KONEC = "END"

DATA = """


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

slova = []
pocty = []

def PridejSlovo(slovo):
    if slovo in slova:
        pocty[slova.index(slovo)] += 1
    else:
        slova.append(slovo)
        pocty.append(1)

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
        nejpocet = max(pocty)
        kde = pocty.index(nejpocet)
        nejslovo = slova[kde]
        pocty[kde] = 0
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