

with open("Programovani_9_1_2024.py", "r", encoding="utf-8") as soubor:
    for radka in soubor:
        print(radka, end="")


f = open("Programovani_9_1_2024.py", "r", encoding="utf-8")
for radka in f:
    print(radka, end="")
f.close()

def Cisla():
    c = 1
    while True:
        yield c
        c += 1

cisla = Cisla()
print( next (cisla))
print( next (cisla))
print( next (cisla))
print( next (cisla))

def PrectiRadky1():
    """vrací postupně"""
    vstup = []
    while (s:= input()) != "":
        yield s 

radky = PrectiRadky1()

soucet = 0
for r in radky:
    soucet += int(r)
    print(f"+{int(r)} = {soucet}")

print(f"soucet = {soucet}")
print(radky)


def PrectiRadky():
    vstup = []
    while (s:= input()) != "":
        vstup.append(s)
    return vstup

radky = PrectiRadky()
soucet = 0
for r in radky:
    soucet += int(r)
    print(f"+{int(r)} = {soucet}")

print(f"soucet = {soucet}")
print(radky)


def pricti(y):
    def soucet(x):
        return x+y
    return soucet

pricti_1 = pricti(1)
print(pricti_1(25))
pricti_100 = pricti(100)
print(dir(pricti_100))
print(pricti_100.__code__.co_freevars)
print(pricti_100.__closure__[0].cell_contents)