def je_to_datum(vstup):
    vstup = vstup.split(".")
    #musi mit tri casti - rok, mesic, den
    if len(vstup) != 3:
        return False
    #casti musi byt spravne dlouhe
    if len(vstup[0]) != 2 or len(vstup[1]) != 2 or len(vstup[2]) != 4:
        return False
    for i in range(len(vstup)):
        try:
            vstup[i] = int(vstup[i])
        except:
            return False #pokud to nejsou cisla, format je spatne
    rok = vstup[2]
    mesic = vstup[1]
    den = vstup[0]
    if rok < 0: #kdyby bylo zadano zaporne cislo, neni to rok
        return False
    if mesic > 12 or mesic < 1:
        return False
    #jaky je maximalni mozny den v danem mesici:
    if mesic == 2:
        if rok%4 != 0 or (rok%4 == 0 and rok%100 == 0 and rok%400 != 0):
            max_den = 28
        else:
            max_den = 29
    elif mesic in [1,3,5,7,8,10,12]:
        max_den = 31
    else:
        max_den = 30
    if den < 0 or den > max_den:
        return False
    return True #pokud splnuje vsechny podminky, je to datum        

def je_to_cas(vstup):
    vstup = vstup.split(":")
    #musi mit tri casti - hodiny, minuty, vteriny
    if len(vstup) != 3:
        return False
    #casti musi byt spravne dlouhe:
    for i in vstup:
        if len(i) != 2:
            return False
    #musi to byt cisla
    for i in range(len(vstup)):
        try:
            vstup[i] = int(vstup[i])
        except:
            return False
    hodiny = vstup[0]
    minuty = vstup[1]
    sekundy = vstup[2]
    if hodiny < 0 or hodiny > 23:
        return False
    if minuty < 0 or minuty > 59 or sekundy < 0 or sekundy > 59:
        return False
    return True

def vypocet_casu(zacatek_cas, konec_cas):
    celkem = [0,0,0] #hodiny, minuty, sekundy
    zacatek_cas = zacatek_cas.split(":")
    konec_cas = konec_cas.split(":")
    drzim_si = 0
    for i in range(2,-1,-1):
        konec_cas[i] = int(konec_cas[i])
        zacatek_cas[i] = int(zacatek_cas[i])
        zacatek_cas[i] += drzim_si
        if konec_cas[i] < zacatek_cas[i]:
            konec_cas[i] += 60
            drzim_si = 1
        else:
            drzim_si = 0
        celkem[i] = konec_cas[i] - zacatek_cas[i]
    return celkem

def prihradkove_trideni(vstup):
    for j in range(2,-1,-1):
        if j == 2 or j == 1:
            max_hodnota = 60
        else:
            max_hodnota = 9999
        pocty = max_hodnota*[0]
        for aktivita in vstup:
            cas = aktivita[0]
            cislo = cas[j]
            pocty[cislo] += 1
        #kumulovane cetnosti:
        suma = 0
        for i in range(max_hodnota):
            pocty[i], suma = suma, pocty[i] + suma
        vystup = [None]*len(vstup)
        for aktivita in vstup:
            cas = aktivita[0]
            cislo = cas[j]
            vystup[pocty[cislo]] = [cas, aktivita[1]]
            pocty[cislo] += 1
        vstup = vystup
    return vystup
    
aktivity = {}

radek_vstupu = input()
while radek_vstupu != ".":
    rozsekany_radek = radek_vstupu.split()
    
    #kontrola jestli radek splnuje format

    if len(rozsekany_radek) >= 5: # pokud odpovida format, podminka bude platit. Zajistuje nam, ze indexy budou existovat
        zacatek_datum = rozsekany_radek[0]
        zacatek_cas = rozsekany_radek[1]
        konec_datum = rozsekany_radek[-2]
        konec_cas = rozsekany_radek[-1]
        if (je_to_datum(zacatek_datum) == True) and (je_to_cas(zacatek_cas) == True) and (je_to_datum(konec_datum) == True) and (je_to_cas(konec_cas) == True):
            prostredek = rozsekany_radek[2:-2]
            nazev_aktivity = ""
            for i in prostredek:
                nazev_aktivity += i
                nazev_aktivity += " "
            nazev_aktivity = nazev_aktivity[:-1]

            #pridani aktivity_do_slovniku

            if nazev_aktivity in aktivity:
                celkem_predtim = aktivity[nazev_aktivity]
                celkem_novy = vypocet_casu(zacatek_cas, konec_cas)
                celkem = [0,0,0]
                drzim_si = 0
                for i in range(2,-1,-1):
                    celkem[i] = celkem_predtim[i] + celkem_novy[i]
                    celkem[i] += drzim_si
                    if celkem[i] > 59 and i != 0:
                        drzim_si = 1
                        celkem[i] -= 60
                    else:
                        drzim_si = 0
            else:   
                celkem = vypocet_casu(zacatek_cas, konec_cas)
            aktivity[nazev_aktivity] = celkem

    radek_vstupu = input()

aktivity_seznam = []
for aktivita in aktivity:
    aktivity_seznam.append([aktivity[aktivita], aktivita]) 

setridene_casy = prihradkove_trideni(aktivity_seznam)

for i in range(len(setridene_casy)-1,-1,-1):
    zaznam = setridene_casy[i]
    cas = zaznam[0]
    aktivita = zaznam[1]
    for j in range(3):
        cas[j] = "{:02d}".format(cas[j])
    print(*cas,sep=":",end=" ")
    print(aktivita)