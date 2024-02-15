from bidict import bidict
prevod = bidict({"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15})

def preved_z_n_soustavy(cislo, n):
    cislo_pozpatku = cislo[-1::-1]
    hodnota = 0
    mocnina = 0
    for cislice in cislo_pozpatku:
        if cislice in prevod:
            cislice = prevod[cislice]
        hodnota += int(cislice)*(n**mocnina)
        mocnina += 1
    return hodnota

def preved_do_n_soustavy(cislo, n):
    prevedene = ""
    while True:
        zbytek = cislo%n
        if zbytek >= 10:
            zbytek = prevod.inverse[zbytek]
        cislo //= n
        prevedene = str(zbytek) + prevedene
        if cislo == 0:
            break
    return prevedene

print(preved_z_n_soustavy("FF",16))
print(preved_do_n_soustavy(255,16))

vstup = input().split()
soustava1 = int(vstup[0])
cislo1 = (vstup[1])
soustava2 = int(vstup[2])
cislo2 = (vstup[3])
soustava3 = int(vstup[4])

cislo1 = preved_z_n_soustavy(cislo1, soustava1)
cislo2 = preved_z_n_soustavy(cislo2, soustava2)

preved_do_n_soustavy(cislo1+cislo2, soustava3)
preved_do_n_soustavy(cislo1-cislo2, soustava3)
preved_do_n_soustavy(cislo1*cislo2, soustava3)
preved_do_n_soustavy(cislo1//cislo2, soustava3)