def zpracuj_vstup():

    pocet_kostek = "-"

    while pocet_kostek == "-":
        radek = input().split()
        if len(radek) != 0:
            pocet_kostek = int(radek[0])

    cisla = []
    ukazatel_radku = 1

    while len(cisla) != 2*pocet_kostek:
        if ukazatel_radku < len(radek):
            cisla.append(int(radek[ukazatel_radku]))
            ukazatel_radku += 1
        else:
            radek = input().split()
            ukazatel_radku = 0

    kostky = []
    for kolikata in range(pocet_kostek):
        kostky.append(cisla[0+2*kolikata : 2+2*kolikata])

    return kostky

def nejdelsi_rada(kostky):
    
    def rozsir_radu(z_ceho, zbyvajici_kostky):
        rozsireni = []
        for kostka in zbyvajici_kostky:
            if kostka[0] == z_ceho[1]:
                rozsireni.append(kostka)
            elif kostka[1] == z_ceho[1]:
                rozsireni.append([kostka[1],kostka[0], "naruby"])
        return rozsireni
    
    nejdelsi = 0

    def rada(aktualni, zbyva):
        nonlocal nejdelsi

        na_vyber = rozsir_radu(aktualni[-1], zbyva)
        
        vyzkousene_kostky = set()
        for kostka in na_vyber:
            if tuple(kostka) not in vyzkousene_kostky: 
                nove_aktualni = aktualni + [kostka]
                nove_zbyva = list(zbyva)
                if len(kostka) > 2:
                    nove_zbyva.remove([kostka[1],kostka[0]])
                else:
                    nove_zbyva.remove(kostka)
                rada(nove_aktualni, nove_zbyva)
                vyzkousene_kostky.add(tuple(kostka))

        delka = (len(aktualni))
        #print(delka)
        if delka > nejdelsi:
            nejdelsi = delka
    
    def zacni_vsemi_kostkami():
        vyzkousene_kostky = set()
        for kostka in kostky:
            if tuple(kostka) not in vyzkousene_kostky:
                nove_kostky = list(kostky)
                nove_kostky.remove(kostka)
                rada([kostka], nove_kostky)
                vyzkousene_kostky.add(tuple(kostka))
        kostky_naruby = [[kostka[1],kostka[0]] for kostka in kostky if kostka[0] != kostka[1]]
        for kostka in kostky_naruby:
            if tuple(kostka) not in vyzkousene_kostky:
                nove_kostky = list(kostky_naruby)
                nove_kostky.remove(kostka)
                rada([kostka], nove_kostky)
                vyzkousene_kostky.add(tuple(kostka))
    
    zacni_vsemi_kostkami()
    #print()
    print(nejdelsi)

kostky = zpracuj_vstup()
nejdelsi_rada(kostky)
    
