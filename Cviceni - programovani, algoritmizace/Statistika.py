seznam = []
x = int(input())
while x!= -1:
    seznam.append(x)
    x = int(input())

def minimalni_cislo(seznam):
    nejmensi = seznam[0]
    for i in seznam:
        if i < nejmensi:
            nejmensi = i
    return nejmensi

def maximalni_cislo(seznam):
    nejvetsi = seznam[0]
    for i in seznam:
        if i > nejvetsi:
            nejvetsi = i
    return nejvetsi

def soucet_cisel(seznam):
    soucet = 0
    for i in seznam:
        soucet += i
    return soucet

def aritmeticky_prumer(seznam):
    soucet = soucet_cisel(seznam)
    prumer = soucet//len(seznam)
    return prumer

def rozsah(seznam):
    nejmensi = minimalni_cislo(seznam)
    nejvetsi = maximalni_cislo(seznam)
    rozsah_cisel = nejvetsi-nejmensi+1
    return rozsah_cisel

print(rozsah(seznam))
print(aritmeticky_prumer(seznam))
print(minimalni_cislo(seznam))
print(maximalni_cislo(seznam))
print(soucet_cisel(seznam))