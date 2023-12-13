def udelej_cisla(vstup):
    """ze seznamu, kde jsou jednotlive cislice zapsany zvlast a jako retezce, vyrobi seznam, 
    kde jsou cisla zapsana jako integery a cele cislo je jedna polozka"""
    #v promenne hodnota je ulozen soucet aktualne tvoreneho cisla
    hodnota = 0
    #v promenne index jsou ulozeny indexy vsech polozek na kterych jsme nasli cislice naseho aktualniho cisla
    index = []
    #v promenne ztraceno je ulozeno o kolik mensi je nas novy seznam oproti staremu, potrebujeme to pro posouvani indexu,
    #indexy, ktere mame nahradit mame vuci staremu seznamu, ale my potrebujeme nahrazovat hodnoty v tom starem
    ztraceno = 0
    #pres seznam vstup iterujeme, a tedy ho nemuzeme zaroven menit, proto mame seznam novy
    novy = list(vstup)
    for i in range(len(vstup)):
        znak = vstup[i]
        if znak in cislice:
            #pokud je aktualni znak cislice, ulozime si index na kterem jsme ho nasli
            index.append(i)
            #nasi stavajici hodnotu posuneme o jeden rad, a pripocteme hodnotu cislice na rad jednotek
            hodnota *= 10
            hodnota += int(znak)
        #jakmile najdeme znak ktery neni cislici, cislo jiz skoncilo, muzeme ho ulozit a nahradit
        #take musime osetrit pripad, kdyby cislice, byla posledni ve vstupu
        if znak not in cislice or i == (len(vstup)-1):
            if index != []:
                #budeme nahrazovat usek od indexu prvni cislice az po index posledni cislice
                #cely usek bude posunut o tolik mist, o kolik je nas novy seznam mensi nez puvodni
                pocatecni_index = index[0] - ztraceno
                konecny_index = index[-1] - ztraceno
                novy[pocatecni_index : konecny_index + 1] = [hodnota]
                #pripocteme pocet ztracenych indexu
                ztraceno += (konecny_index - pocatecni_index)
                #vynulujeme hodnotu a indexy
                hodnota = 0
                index = []
    return novy

def vyhodnot(vstup):
    """rekurzivni funkce, ktera postupne podle priorit vyhodnoti cely vyraz"""

    #projdeme vzdy cely vyraz zleva doprava, zvlast pro kazdy operator a to v poradi podle jejich priorit
    
    #zavorky

    #zasobnik na uzavirani zavorek pro pripad vice zavorek vnorenych v sobe
    #nemuzeme hledat jen nejakou ")", potrebujeme tu nasi
    zasobnik = []
    for i in range(len(vstup)):
        znak = vstup[i]
        if znak == "(":
            #v okamziku, kdy zavorku otevreme, vlozime ji do zasobniku, kde ceka dokud ji neuzavreme
            zasobnik.append(znak)
            #hledame tak dlouho, dokud neuzavreme prvni zavorku, kterou jsme otevreli
            while zasobnik != []:
                #chceme prohledat zbytek
                for j in range(i+1,len(vstup)):
                    dalsi_znak = vstup[j]
                    #pokud najdeme zavřenou závorku, uzavřeme tu, kterou jsme jako poslední otevřeli
                    if dalsi_znak == ")":
                        zasobnik.pop()
                        if zasobnik == []:
                            break
                    elif dalsi_znak == "(":
                        zasobnik.append("(")
            #jakmile uzavřeme vnější závorky, zbyde nám na indexu i ta první otevřená a na indexu j ta, která ji zavírá
            #tento úsek (tj. to co je uvnitř závorky a ty samotné znaky závorek) chceme nahradit hodnotou výpočtu v závorce
            vstup[i:j+1] = vyhodnot(vstup[i+1:j])
            #pokud nám již nezbývá, co projít, chceme se přesunout na další operaci
            if len(vstup) - 1 < i + 1:
                break
        if len(vstup) - 1 < i + 1:
                break
    
    #unarni minus
    
    if "(" not in vstup:
        znak = vstup[0]    
        #unarni minus pred sebou nebude mit nic
        if znak == "-":
            #za unarnim minusem bude vzdy cislo (zavorky jiz byly odstranene), cokoli jineho nema prednost
            cislo = vstup[1]
            #minus a cislo nahradime vysledkem po provedeni operace
            vstup[:2] = operace(cislo, "-")

    #nasobeni

    for i in range(len(vstup)):
        znak = vstup[i]
        if znak == "*":
            #pred a za krat bude vzdy cislo (vse s vyssi prioritou jiz bylo odstraneno)
            leve_cislo = vstup[i-1]
            prave_cislo = vstup[i+1]
            vstup[i-1:i+2] = operace(prave_cislo, "*", leve_cislo)
            if len(vstup) - 1 < i + 1:
                break
        if len(vstup) - 1 < i + 1:
            break
    
    #scitani a odcitani

    if "(" not in vstup and "*" not in vstup:
        for i in range(len(vstup)):
            znak = vstup[i]
            if znak == "+" or znak == "-":
                leve_cislo = vstup[i-1]
                prave_cislo = vstup[i+1]
                operator = znak
                vstup[i-1:i+2] = operace(prave_cislo, operator, leve_cislo)
                if len(vstup) - 1 < i + 1:
                    break
            if len(vstup) - 1 < i + 1:
                break

    return vstup


def operace(prave_cislo, operator, leve_cislo=None):
    if operator == "-" and leve_cislo == None:
        vysledek = -prave_cislo
    elif operator == "*":
        vysledek = leve_cislo * prave_cislo
    elif operator == "+":
        vysledek = leve_cislo + prave_cislo
    elif operator == "-":
        vysledek = leve_cislo - prave_cislo 
    return [vysledek]

cislice = ["0","1","2","3","4","5","6","7","8","9"]
operatory = ["-","*","+"]

vstup = input()
#ze vstupu chceme udelat seznam
vstup = list(vstup)
#vsechna cislice nahradime cisly
vstup = udelej_cisla(vstup)
#ve vysledku by mela zustat jen jedna polozka, vysledek
vyhodnocene = vstup
while len(vyhodnocene) != 1:
    vyhodnocene = vyhodnot(vyhodnocene)
print(vyhodnocene[0])