def zpracuj_vstup():

    pocet_prekazek = "-"

    while pocet_prekazek == "-":
        radek = input().split()
        if len(radek) != 0:
            pocet_prekazek = int(radek[0])

    souradnice = []
    ukazatel_radku = 1

    while len(souradnice) != 2*pocet_prekazek + 4:
        if ukazatel_radku < len(radek):
            souradnice.append(radek[ukazatel_radku])
            ukazatel_radku += 1
        else:
            radek = input().split()
            ukazatel_radku = 0

    prekazky = souradnice[:2*pocet_prekazek]
    start = souradnice[2*pocet_prekazek : 2*pocet_prekazek+2]
    cil = souradnice[2*pocet_prekazek+2:]

    return prekazky, start, cil

prekazky, start, cil = zpracuj_vstup()

