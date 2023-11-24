def je_cislo_dobre(cislo):   
    rad = 10
    while cislo%rad != cislo:
        rad *= 10
    rad_zbytku = rad//10
    zbytek = cislo%rad_zbytku
    cislice = (cislo%rad - zbytek)//(rad_zbytku)
    while rad != 1:
        if cislice == 0:
            return False
        if cislo%cislice != 0:
            return False
        rad //= 10
        rad_zbytku = rad/10
        zbytek = cislo%rad_zbytku
        cislice = (cislo%rad - zbytek)//(rad_zbytku)
    return True

n = int(input())

pocet = 0
for i in range(1,n+1):
    vysledek = je_cislo_dobre(i)
    if vysledek == True:
        pocet += 1

print(pocet)
