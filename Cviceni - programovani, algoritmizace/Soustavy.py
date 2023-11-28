def preved_z_n_soustavy(cislo, n):
    cislo_pozpatku = cislo[-1::-1]
    hodnota = 0
    mocnina = 0
    for cislice in cislo_pozpatku:
        hodnota += int(cislice)*(n**mocnina)
        mocnina += 1
    return hodnota

def preved_do_n_soustavy(cislo, n):
    prevedene = ""
    while cislo//n != 0:
        zbytek = str(cislo%n)
        cislo //= n
        prevedene = zbytek + prevedene
    zbytek = str(cislo%n)
    cislo //= n
    prevedene = zbytek + prevedene
    print(prevedene)

n1 = 16
while True:
    vstup = input()
    vstup = preved_z_n_soustavy(vstup,n1)

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