"""
Náhodně generované sudoku
Veronika Kavanová, 1. ročník bakalářského programu, obor Informatika, kruh 35
zimní semestr 2023/24
Programování NPRG030
"""

import random

def print_sudoku(policka):
    for i in range(81):
        pole = policka[i]
        if pole.hodnota == None:
            print("-", end="")
        else:
            print(pole.hodnota, end="")
        if i % 3 == 2:
            print("     ", end="")
        if i % 9 == 8:
            print()

class policko:
    """Třída pro jedno políčko v sudoku, o každém políčku je uložena jeho hodnota, seznam jeho sousedů (tj. políček, která 
    ho ovlivňují) a seznam možných hodnot - tj. čísel, která do políčka můžeme napsat."""
    def __init__(self, sousedi = None, hodnota = None, mozne_hodnoty = [1,2,3,4,5,6,7,8,9]):
        self.sousedi = sousedi
        self.hodnota = hodnota
        self.mozne_hodnoty = mozne_hodnoty
    
    def vepis_hodnotu(self, hodnota):
        """Funkce, která změní atribut hodnota daného políčka a odstraní tuto hodnotu z možných hodnot všech sousedů
        tohoto políčka."""
        self.hodnota = hodnota
        for soused in self.sousedi:
            soused.mozne_hodnoty = odstran_hodnotu_ze_seznamu(soused.mozne_hodnoty, hodnota)

    def smaz_hodnotu(self):
        """Funkce, která změní atribnut hodnota daného políčka na None a zkontroluje všechny sousedy, jestli se jim
        nemá vrátit hodnota do seznamu možných hodnot."""

        #Odstranění hodnoty z tohoto políčka mohlo způsobit, že už tato hodnota v sousedních políčkách být může, \
        #ale také je možné, že ji stále blokují jiná políčka. Proto budeme muset u sousedů prozkoumat všechny jejich \
        #sousedy, zda se v nich daná hodnota vyskytuje nebo ne.

        #Na to budeme potřebovat hodnotu znát, ale nechceme, aby pole, ze kterého hodnotu mažeme, mátlo výsledky, \
        #proto smazáním musíme začít.
        puvodni_hodnota = self.hodnota
        self.hodnota = None

        for soused in self.sousedi:
            #Pokud žádný soused daného souseda nebude mít hodnotu stejnou jako tu, která byla v našem políčku, \
            #zadny_konflikt zůstane True a můžeme tuto hodnotu vrátit zpět do seznamu možných hodnot.
            zadny_konflikt = True
            for soused_z_druheho_kolena in soused.sousedi:
                if soused_z_druheho_kolena.hodnota == puvodni_hodnota:
                    #Pokud jsme narazili na souseda souseda, který danou hodnotu má, tak nemusíme kontrolovat ostatní \
                    #již víme, že tato hodnota i nadále v políčku být nemůže a seznam možných hodnot se tedy nemění.
                    zadny_konflikt = False
                    break
            if zadny_konflikt == True:
                soused.mozne_hodnoty += [puvodni_hodnota]
    
def odstran_hodnotu_ze_seznamu(seznam, hodnota):
    """Vytvoří a vrátí nový upravený seznam bez dané hodnoty. Odstraní pouze jeden výskyt, a proto ji využíváme pouze 
    pro seznamy s neopakujícími se hodnotami. Upravuje pouze jen daný výskyt seznamu."""
    if hodnota in seznam:
        index_hodnoty = seznam.index(hodnota)
        seznam = seznam[:index_hodnoty] + seznam[index_hodnoty + 1:]
    return seznam

def vygeneruj_sudoku(): 
    """Funkce, která si řekne uživateli o počet číslic a vygeneruje náhodnou řešitelnou sudoku s takovýmto počtem známých 
    číslic."""

    def generuj_prazdnou_sudoku():
        """Funkce, která vygeneruje seznam 82 políček sudoku a nadefinuje jejich sousedy.."""
        
        policka = [policko() for _ in range(82)] #Vytvoří seznam všech políček v sudoku.
        #Seznam má 82 políček, to poslední je zarážka pro funkci vypln_pole(), kterou budeme využívat na vyplňování sudoku. \
        #Tomuto políčku sousedy přiřazovat nebudeme, jelikož není součástí sudoku.
        
        #Políčka budeme v seznamu číslovat po řádcích, tj. policko na indexu 9, bude na druhém řádku v prvním sloupci.;

        #Tento cyklus přiřadí všem polím jejich sousedy (při vytvoření seznamu byla množina sousedů zatím prázdná)
        for radek in range(9):
            for sloupec in range(9):
                pole = policka[radek*9 + sloupec]
                #Vytvoříme množinu sousedů ve které budou nejprve políčka ve stejném řádku. 
                #To, že je to množina nám umožní se vyhnout duplikátům
                sousedi = {policka[radek*9 + j] for j in range(9) if j != sloupec} 
                #Přidáme sousedy ve stejném sloupci,
                sousedi.update(policka[i*9 + sloupec] for i in range(9) if i != radek)
                #Získáme řádek a sloupec na kterém začíná čtverec 3*3 ve kterém se pole nachází 
                ctverec_radek, ctverec_sloupec = (radek//3)*3, (sloupec//3)*3 
                #Přidáme do množiny sousedy ve stejném 3*3 čtverci. 
                #Ty, které jsou na stejném řádku či sloupci jako pole, už jsme přidali, nemusíme je tedy znovu přidávat.
                sousedi.update(policka[(ctverec_radek + i)*9 + (ctverec_sloupec + j)] \
                    for i in range(3) for j in range(3) if (ctverec_radek + i != radek or ctverec_sloupec + j != sloupec))
                pole.sousedi = sousedi

        return policka

    def generuj_plnou_sudoku(policka):
        """Funkce, která do všech políček doplní hodnotu, tak, aby byly splněny pravidla sudoku. Tj. aby se v každém 
        řádku, sloupci a čtverci 3*3 vyskytovaly všechny číslice 1-9 právě jednou."""

        def vypln_pole(pole, policka, hotovo):
            """Rekurzivní funkce, která do jednoho pole zkusí vepsat hodnotu, pokud to nejde, vrátí se zpět k předchozímu poli 
            (backtracking) a tam napíše jinou hodnotu.
            pole: pole do kterého vepisujeme
            policka: seznam všech políček
            hotovo: počet políček, do kterých jsme už vepsali hodnotu, umožní nám ukončit rekurzi a pomocí indexů se přesunout 
                na další políčko
            """

            #Ukončení rekurze, úspěšně jsme vyplnili všechna políčka
            if hotovo == 81:
                return policka
            
            #V seznamu jeste_nezkuseno budeme mít uloženy všechny hodnoty, které do pole můžeme vepsat a ještě jsme je \
            #nezkusili. Na začátku jsou to všechny hodnoty, které v poli být můžou. Pokaždé, když nějakou hodnotu zkusíme \
            #vepsat, ji ze seznamu odstraníme. 
            jeste_nezkuseno = pole.mozne_hodnoty

            #Na začátku je vysledek False - ještě jsme nezískali, to, co jsme potřebovali. Dokud tomu tak bude, \
            #tj. další políčko se nám nepodařilo vyplnit, tak budeme zkoušet jiné hodnoty, pokud jsme již vyzkoušeli všechno, \
            #tak vrátíme False o level výš. 
            vysledek = False

            while vysledek == False:
            
                #Pokud neexistuje hodnota, kterou bychom do pole mohli doplnit, vyplnění předchozích políček není vhodné a \
                #musíme se vrátit zpět k předchozímu políčku.
                if jeste_nezkuseno == []:
                    return False

                nova_hodnota = random.choice(jeste_nezkuseno)
                jeste_nezkuseno = odstran_hodnotu_ze_seznamu(jeste_nezkuseno, nova_hodnota)
                pole.vepis_hodnotu(nova_hodnota)

                #Když jsme měli předtím hotovo např. 0 políček, tak teď jsme dělali nulté a teď se přesouváme na první
                nove_pole = policka[hotovo+1]

                #Když jsme vepsali do políčka možnou hodnotu, zkusíme s takto vyplněnou sudoku vyplnit další políčko
                vysledek = vypln_pole(nove_pole, policka, hotovo + 1)
                #Pokud je vysledek False, znamená to, že v dalším poli - nove_pole nemůže být nic vepsáno. Proto chceme \
                #v tomto poli zkusit jinou hodnotu, a proto nejprve musíme smazat aktuální hodnotu, která tam teď byla.
                if vysledek == False:
                    pole.smaz_hodnotu()
            
            #Pokud se nám vrátí místo False seznam policek, while cyklus skončí a seznam políček vrátíme o level výš. \
            #Našli jsme vhodné vyplnění.
            return policka

        #Funkci vypln_pole spustíme na prvním poli v seznamu, ostatní pole se vyplní rekurzivně.
        pole = policka[0]
        policka = vypln_pole(pole, policka, 0)
        #82. políčko v seznamu tam bylo pouze jako zarážka pro funkci vypln_pole a proto se ho teď můžeme zbavit.
        policka.pop()

        return policka

    def jedno_reseni(policka, prazdna_policka):
        """Funkce, která zjistí, jestli má dané sudoku právě jedno řešení. Výsledek je True pokud ano, False pokud ne.
        Slouží k zjištění, zda můžeme dané políčko smazat nebo ne.
        policka: seznam všech políček
        prazdna_policka: seznam prázdných políček
        """

        def unikatni_reseni(policka, prazdna_policka):
            """Rekurzivní funkce, která se snaží doplnit řešení do plného. Vrací False pokud už jsme našli více řešení
            nebo pokud daná pozice nemá řešení, True pokud jsme dokončili celé řešení.
            """

            #Pokud najdeme řešení, potřebujeme vědět kolik řešení jsme již našli, jelikož chceme, aby každé volání funkce \
            #mohlo skončit, jakmile někde najdeme druhé řešení.
            nonlocal reseni
            
            #Pokud má nějaké prázdné políčko jen jednu možnou hodnotu, která se do něj může zapsat, je to jediná \
            #možnost, a tudíž ji tam prostě zapíšeme. 
            
            opakovat = True
            while opakovat == True:
                
                if prazdna_policka != []:
                    pole_s_nejmene_volbami = prazdna_policka[0]

                for pole in prazdna_policka:
                    
                    #pokud políčko nemá žádné možnosti, znamená to, že jsme někde při náhodné volbě vybrali špatně, \
                    #chceme se tedy vrátit do stavu před volbou. To uděláme ukončením volání funkce. Vrátíme False, \
                    #abychom naznačili, že cesta nevedla k řešení
                    if len(pole.mozne_hodnoty) == 0:
                        return False
                        
                    elif len(pole.mozne_hodnoty) == 1:
                        pole.vepis_hodnotu(pole.mozne_hodnoty[0])
                        #políčko už není prázdné
                        prazdna_policka = odstran_hodnotu_ze_seznamu(prazdna_policka, pole)
                        #zapsali jsme hodnotu a chceme opět zkusit projít všechna políčka, chceme projít i ty, které \
                        #jsme předtím už prošli, jelikož teď se situace mohla změnit
                        break
                    
                    else:
                        if len(pole.mozne_hodnoty) < len(pole_s_nejmene_volbami.mozne_hodnoty):
                            pole_s_nejmene_volbami = pole
                
                else:
                    opakovat = False
                    
            #jakmile skončí for loop, žádné políčko už nemá pouze jednu možnost

            #pokud jsme zaplnili všechna políčka, dokončili jsme řešení. 
            if prazdna_policka == []:
                return True
            
            #Pokud existují políčka s více možnostmi, náhodně jedno vybereme. A postupně prozkoumáme, co se stane, \
            #když do něj zkusíme vepsat všechny možné hodnoty
            pole = pole_s_nejmene_volbami
            
            for hodnota in pole.mozne_hodnoty:
                
                #print_sudoku(policka)
                #print(f"index: {policka.index(pole)}. Hodnota: {hodnota}.")
            
                pole.vepis_hodnotu(hodnota)
                nova_prazdna_policka = odstran_hodnotu_ze_seznamu(prazdna_policka, pole)
                #zkusíme do políčka vepsat tuto hodnotu a rekurzivně prozkoumat, kam to povede
                vysledek = unikatni_reseni(policka, nova_prazdna_policka)
                
                #print(vysledek)

                #pokud je výsledek True, tak jsme našli řešení, jejich počet se zvětší o 1
                if vysledek == True:
                    reseni += 1
            
                #Zkontrolujeme počet nalezených řešení. Pokud máme alespoň dvě řešení, rovnou volání ukončíme. \
                #Každé volání, tedy i poslední, od teď vrátí False, protože počet řešení se nemůže zmenšit.
                if reseni > 1:
                    return False

                for jedno_pole in prazdna_policka:
                    jedno_pole.smaz_hodnotu()

        #nejprve jsme nenašli ani jedno řešení
        reseni = 0
        vysledek = unikatni_reseni(policka, prazdna_policka)
        if vysledek == None:
            if reseni == 1:
                vysledek = True
        #během testování jsme do původně prázdných políček zapisovali, chceme vše vrátit do původního stavu
        for pole in prazdna_policka:
            pole.smaz_hodnotu()

        return vysledek
    
        
        def zjisti_pocet_policek():
            """Funkce, která od uživatele zjistí kolik počet políček, chce mít na začátku v sudoku vyplněných"""
            hotovo = False
            while hotovo == False:
                znat = input("Kolik si přeješ aby v sudoku bylo vyplněných polí? Zadej číslo od 25 do 81. \n")
                try:
                    znat = int(znat)
                    if znat < 17:
                        print("Sudoku s méně než 17 odhalenými číslicemi nikdy nebude mít pouze jedno řešení. Musíš zadat větší číslo.")
                    elif znat > 81:
                        print("Tolik číslic v sudoku není")
                    elif znat < 25:
                        print("I když sudoku mohou mít takový počet číslic, není jich mnoho a jejich nalezení by mohlo trvat dlouho.")
                    else:
                        hotovo = True
                except ValueError:
                    print("Musíš zadat číslo pomocí číslic.")
            return znat

        def odstran_pole(policka, vyplnena_policka, prazdna_policka, odstraneno: int):
            """Rekurzivní funkce, která se pokusí rekurzivně odstranit daný počet polí, tak aby stále sudoku mělo právě
            jedno řešení.
            Policka: seznam všech políček
            Vyplnena_policka: seznam políček ve kterých je nějaká hodnota
            Prazdna_policka: seznam prázdných políček
            odstraneno: počet políček, které jsme již odstranili
            """

            #pokud jsme již odstranili požadovaný počet políček (uložený v konstantě odstranit), chceme ukončit \
            #volání všech funkcí

            if odstraneno == odstranit:
                return policka

            #jeste_nezkuseno bude náš seznam všech políček, které jsme ještě nezkusili odstranit
            jeste_nezkuseno = vyplnena_policka

            #funkce bude fungovat podobně jako rekurzivní funkce vypln_pole
            
            #nejprve ještě nemáme výsledek
            vysledek = False

            #zkoušíme mazat políčka dokud nenajdeme vyhovující
            while vysledek == False:
                
                #pokud už jsme všechno zkusili a nic nefunguje, problém nastal někdy předtím
                if jeste_nezkuseno == []:
                    return False
    
                #vybereme náhodné pole a pokusíme se jej odstranit    
                pole = random.choice(jeste_nezkuseno)

                #print(f"Odstraneno: {odstraneno}, pole: {policka.index(pole)}")

                stara_hodnota = pole.hodnota
                pole.smaz_hodnotu()

                #updatujeme naše seznamy
                jeste_nezkuseno = odstran_hodnotu_ze_seznamu(jeste_nezkuseno, pole)
                nova_prazdna_policka = prazdna_policka + [pole]

                #otestujeme zda dané sudoku má právě jedno řešení 
                unikatni = jedno_reseni(policka, nova_prazdna_policka)
                #print_sudoku(policka)
                #print(unikatni)

                #pokud ne, nemůžeme smazat tohle políčko, a musíme do něj jeho hodnotu vepsat zpátky
                if unikatni == False:
                    pole.vepis_hodnotu(stara_hodnota)
                #pokud ano, můžeme zkusit smazat další políčko
                else:
                    nova_vyplnena_policka = odstran_hodnotu_ze_seznamu(vyplnena_policka, pole)
                    vysledek = odstran_pole(policka, nova_vyplnena_policka, nova_prazdna_policka, odstraneno+1)
                    if vysledek == False:
                        pole.vepis_hodnotu(stara_hodnota)
                    #pokud se nám další pole odstranit nepodaří, výsledek bude stále False a zkusíme místo tohoto nějaké \
                    #jiné. Pokud dojdeme až na konec výsledek už False nebude a while loop skončí

            return policka
        
        #v proměnné policka je uložený seznam všech zatím prázdných políček sudoku    
        #policka = generuj_prazdnou_sudoku()
        
        #do každého políčka uložíme náhodnou možnou hodnotu. Políčka procházíme rekurzivně s použitím backtrackingu
        #začneme prvním polem
        #pole = policka[0]
        #policka = vypln_pole(pole, policka, pole.mozne_hodnoty, 0)

        #na konci seznamu policka je prázdné políčko, které sloužilo jako zarážka pro vypln_pole, toho se nyní můžeme \
        #zbavit
        #policka.pop()

        #V proměnné znát je počet políček, které mají být vyplněné na začátku 
        znat = zjisti_pocet_policek()
        #v proměnné odstranit je počet políček, které musíme vymazat z plně vyplněné sudoku. Proti ní se bude porovnávat \
        #funkce odstran_pole, která bude kontrolovat, zda už daný počet polí odstranila
        odstranit = 81 - znat

        #odstartujeme rekurzivní funkci odstran_pole na sudoku, kde jsou všechna pole vyplněná. Na konci bude v seznamu \
        #policka uloženo sudoku, které může hráč začít řešit

        vysledek = False

        while vysledek == False:
            policka = generuj_prazdnou_sudoku()
            policka = generuj_plnou_sudoku(policka)
            vysledek = odstran_pole(policka, policka, [], 0)
            print(".")
        
        policka = vysledek
        print_sudoku(policka)

        return policka
    
def grafika():
    pass

policka = vygeneruj_sudoku()

