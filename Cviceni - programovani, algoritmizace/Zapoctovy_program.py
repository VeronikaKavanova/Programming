"""
Náhodně generované sudoku
Veronika Kavanová, 1. ročník bakalářského programu, obor Informatika, kruh 35
zimní semestr 2023/24
Programování NPRG030
"""

import random
import pygame

class policko:
    """Třída pro jedno políčko v sudoku.
    self.sousedi: seznam sousedů - políček, které dané políčko ovlivňují - tj. ty ve stejném sloupci, řádku a čtverci 3*3
    self.hodnota: číslo, které je v políčku napsané
    self.mozne_hodnoty: seznam možných hodnot - tj. čísel, která do políčka můžeme napsat. 
    Další čtyři atributy se budou hodit pro řešení sudoku. Slouží pouze pro grafickou stranu programu.
    self.je_prazdne: říká jestli je políčko prázdné, a tedy jestli do něj uživatel může zapisovat. 
    self.vepsana_hodnota: číslo, které uživatel do pole vepsal
    self.vepsane_mozne_hodnoty: seznam čísel, které uživatel zvažuje jako možné
    self.pole_sudoku: zde bude mít každé prázdné policko přiřazené objekt třídy prazdne_pole_sudoku - objekt který slouží \
        pro vykreslování daného políčka."""
    def __init__(self, sousedi = None, hodnota = None, mozne_hodnoty = ["1","2","3","4","5","6","7","8","9"]):
        self.sousedi = sousedi
        self.hodnota = hodnota
        self.mozne_hodnoty = mozne_hodnoty
        #Na začátku atribut je_prazdne nastavíme na False i když to není nejprve pravda. Důvod je ten, že každé pole \
        #nejprve vyplníme a teprve až potom budeme z nějakých políček mazat jejich hodnoty. Tzn. že každé pole se určitě \
        #dostane do stavu je_prazdne = False. 
        self.je_prazdne = False
        self.vepsana_hodnota = None
        self.vepsane_mozne_hodnoty = []
        self.pole_sudoku = None

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

    def aktivni(self, aktivni_policko):
        """Tato funkce se zavolá, když se zmáčkne dané políčko. V případě, že doteď nebylo aktivním, se jím stane, pokud 
        aktivní bylo, tak aktivním být přestane. Vrátí aktivni_policko"""
        #Pokud i před kliknutím toto políčko bylo aktivní, tak nyní aktivním být přestane.
        if self == aktivni_policko:
            aktivni_policko = None
        else:
            aktivni_policko = self
        return aktivni_policko
    
def odstran_hodnotu_ze_seznamu(seznam, hodnota):
    """Vytvoří a vrátí nový upravený seznam bez dané hodnoty. Odstraní pouze jeden výskyt, a proto ji využíváme pouze 
    pro seznamy s neopakujícími se hodnotami. Upravuje pouze jen daný výskyt seznamu."""
    if hodnota in seznam:
        index_hodnoty = seznam.index(hodnota)
        seznam = seznam[:index_hodnoty] + seznam[index_hodnoty + 1:]
    return seznam

def vygeneruj_sudoku(znat: int): 
    """Funkce, která vygeneruje náhodnou řešitelnou sudoku se zadaným počtem známých číslic.
    znat: Počet políček, které si uživatel přeje znát."""

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
            #možnost, a tudíž ji tam prostě zapíšeme. Dál se chceme posunout až pokud už každé políčko má alespoň dvě \
            #možnosti. Proto budeme procházet všechna políčka, a jakmile do některého pole zapíšeme hodnotu, začneme \
            #políčka znovu prohledávat od začátku, jelikož se teď jejich situace mohla změnit.

            opakovat = True
            while opakovat == True:
                
                #Pokud budeme muset pracovat s backtrackingem, budeme chtít pracovat s políčkem s co nejméně možnostmi \
                #toho, co v něm může být napsáno. Musíme mít proti čemu porovnávat, na začátku je to prostě první políčko, \
                #toto políčko musíme znovu určit pokaždé když procházíme seznam všech políček, jelikož jsme mezitím mohli \
                #do tohoto políčka vepsat hodnotu.
                if prazdna_policka != []:
                    pole_s_nejmene_volbami = prazdna_policka[0]

                for pole in prazdna_policka:
                    
                    #Pokud políčko nemá žádné možnosti, znamená to, že už jsme v minimálně druhém volání funkce, a \
                    #při vepsání jedné z možností jsme vybrali špatně, chceme se tedy vrátit do stavu před volbou. To \
                    #uděláme ukončením volání funkce. Vrátíme False, abychom naznačili, že cesta nevedla k řešení.
                    if len(pole.mozne_hodnoty) == 0:
                        return False
                        
                    elif len(pole.mozne_hodnoty) == 1:
                        pole.vepis_hodnotu(pole.mozne_hodnoty[0])
                        #Když jsme do pole vepsali hodnotu, tak už není prázdné.
                        prazdna_policka = odstran_hodnotu_ze_seznamu(prazdna_policka, pole)
                        #Zapsali jsme hodnotu a chceme opět zkusit projít všechna políčka, chceme projít i ty, které \
                        #jsme předtím už prošli, jelikož teď se situace mohla změnit. Toho dosáhneme opustěním for cyklu \
                        #což nás vrátí na konec while cyklu. Jelikož opakovat je stále True, začne while cyklus opět od \
                        #začátku.
                        break
                    
                    else:
                        #Kontrola pole_s_nejmene_volbami má smysl jen pro pole s dvěma a více volbami, jelikož se bude \
                        #využívat až když všechny pole mají alespoň dvě volby.
                        if len(pole.mozne_hodnoty) < len(pole_s_nejmene_volbami.mozne_hodnoty):
                            pole_s_nejmene_volbami = pole
                
                else:
                    #Pokud projdeme celým for cyklem, aniž bychom z něj vystoupili pomocí break, znamená to, že žádné pole \
                    #už nemá jen jednu volbu, a tedy chceme postoupit do další fáze a vystoupit z while cyklu.                    
                    opakovat = False
                    
            #Jakmile skončí for cyklus, žádné políčko už nemá pouze jednu možnost.

            #Pokud jsme zaplnili všechna políčka, dokončili jsme řešení. 
            if prazdna_policka == []:
                return True
            
            #Pokud existují políčka s více možnostmi, vezmeme to s co nejméně možnými hodnotami, které do něj je možné \
            #vepsat. A postupně prozkoumáme, co se stane, když je do něj všechny vepíšeme.
            pole = pole_s_nejmene_volbami
            
            for hodnota in pole.mozne_hodnoty:
                
                pole.vepis_hodnotu(hodnota)
                nova_prazdna_policka = odstran_hodnotu_ze_seznamu(prazdna_policka, pole)
                #Zkusíme do políčka vepsat hodnotu a rekurzivně prozkoumat, kam to povede.
                vysledek = unikatni_reseni(policka, nova_prazdna_policka)
            
                #Pokud je výsledek True, tak jsme dokončili řešení, počet nalezených řešení se zvětší o 1.
                if vysledek == True:
                    reseni += 1
            
                #Zkontrolujeme počet nalezených řešení. Pokud máme alespoň dvě řešení, rovnou volání ukončíme. \
                #Každé volání, tedy i poslední, od teď vrátí False, protože počet řešení je nelokální a nemůže se zmenšit.
                if reseni > 1:
                    return False

                #Pokud budeme prozkoumávat další možné cesty, potřebujeme nejprve vymazat vše, co jsme do políček vepsali. \
                #Tzn. hodnotu kterou jsme zkusili vepsat, a všechny políčka, která jsme vyplnili jako následek tohoto \
                #vepsání. Všechna tato políčka budou v seznamu předtím prázdných políček, jelikož předtím jsme je \
                #odstraňovali pouze ze seznamu nova_prazdna_policka.

                for jedno_pole in prazdna_policka:
                    jedno_pole.smaz_hodnotu()

        #Nejprve jsme nenašli ani jedno řešení
        reseni = 0
        #Chceme zjistit kolik najdeme řešení, když budeme danou sudoku zkoumat.
        vysledek = unikatni_reseni(policka, prazdna_policka)
        #vysledek může být True nebo False nebo None. Funkce vrátí None pokud jsme zkoušeli do jednoho políčka vepsat \
        #všechny možné hodnoty a přitom jsme nenarazili na dvě řešení. Tzn. že volání se neukončilo vrácením False.
        #V takovém případě jsme určitě našli jedno řešení, protože kontrolujeme sudoku vzniklou z hotového řešení, tj. \
        #jedno řešení určitě existuje a druhé jsme nenašli.
        if vysledek == None:
            vysledek = True
        
        #Během zkoumání jsme zapisovali hodnoty do původně prázdných políček. Chceme vše vrátit do původního stavu.
        for pole in prazdna_policka:
            pole.smaz_hodnotu()

        return vysledek
    
    def odstran_pole(policka, vyplnena_policka, prazdna_policka, odstraneno):
        """Rekurzivní funkce, která se pokusí rekurzivně odstranit pole. Pokud má sudoku i po odstranění stále právě 
        jedno řešení, tak se pokusí odstranit další pole.
        policka: seznam všech políček
        vyplnena_policka: seznam políček ve kterých je nějaká hodnota
        prazdna_policka: seznam prázdných políček
        odstraneno: počet políček, které jsme již odstranili, slouží pro ukončení rekurze
        """

        #Funkce bude fungovat podobně jako rekurzivní funkce vypln_pole.

        #Pokud jsme již odstranili požadovaný počet políček (uložený v konstantě odstranit, kterou definujeme ve funkci \
        #vygeneruj_sudoku), chceme ukončit rekurzi a vrátit seznam políček napříč všemi voláními.
        if odstraneno == odstranit:
            return policka

        #jeste_nezkuseno bude náš seznam všech políček, které jsme ještě nezkusili odstranit. Pokaždé když zkusíme nějaké \
        #pole odstranit, odstraníme ho ze seznamu.
        jeste_nezkuseno = vyplnena_policka

        #Na začátku ještě nemáme výsledek.
        vysledek = False

        #Zkoušíme mazat políčka dokud nenajdeme vyhovující.
        while vysledek == False:
            
            #Pokud už jsme zkusili smazat všechna políčka, a nikdy se nám nepodařilo vymazat potřebný počet, problém \
            #nastal někdy předtím a musíme u předchozího políčka zkusit nějaké jiné.
            if jeste_nezkuseno == []:
                return False

            #Z polí, které jsme ještě nezkusili odstranit, vybereme jedno náhodné a pokusíme se jej odstranit    
            pole = random.choice(jeste_nezkuseno)

            #Jeho hodnotu si uložíme, jelikož pokud zjistíme, že smazání nefunuguje, budeme chtít hodnotu vepsat zpět.
            stara_hodnota = pole.hodnota
            pole.smaz_hodnotu()

            jeste_nezkuseno = odstran_hodnotu_ze_seznamu(jeste_nezkuseno, pole)
            nova_prazdna_policka = prazdna_policka + [pole]

            #Otestujeme zda dané sudoku má právě jedno řešení. 
            unikatni = jedno_reseni(policka, nova_prazdna_policka)

            #Pokud ne, nemůžeme toto políčko smazat, a musíme do něj jeho hodnotu vepsat zpátky.
            if unikatni == False:
                pole.vepis_hodnotu(stara_hodnota)
            #Pokud ano, můžeme zkusit smazat další políčko.
            else:
                nova_vyplnena_policka = odstran_hodnotu_ze_seznamu(vyplnena_policka, pole)
                
                #Funkce volá sama sebe. vysledek může být buďto False, pokud jako další nemůžeme smazat žádné políčko.
                #Nebo seznam políček pokud jsme odstranili potřebný počet políček.
                vysledek = odstran_pole(policka, nova_vyplnena_policka, nova_prazdna_policka, odstraneno+1)
                #Pokud je vysledek False, vepíšeme do pole hodnotu zpátky. Vysledek je stále False, a tedy while cyklus
                #pokračuje a zkusí se jiná hodnota.
                if vysledek == False:
                    pole.vepis_hodnotu(stara_hodnota)
        #Pokud je v proměnné vysledek uložený seznam políček, vysledek už není False. While cyklus skončí a my chceme \
        #seznam předat předchozímu volání. Tím se postupně všechny volání ukončí a dostaneme zpět hotový seznam políček
        return policka
    
    #V proměnné policka je uložený seznam všech zatím prázdných políček sudoku. 
    policka = generuj_prazdnou_sudoku()
    #V proměnné policka je teď seznam, který odpovídá hotovému řešení sudoku.
    policka = generuj_plnou_sudoku(policka)

    #V proměnné znát je počet políček, které mají být vyplněné na začátku.
    #V proměnné odstranit je počet políček, které musíme vymazat z plně vyplněné sudoku. Proti ní se bude porovnávat \
    #funkce odstran_pole, která bude kontrolovat, zda už daný počet polí odstranila.
    odstranit = 81 - znat

    #Odstartujeme rekurzivní funkci odstran_pole na sudoku, kde jsou všechna pole vyplněná. Na konci bude v seznamu \
    #policka uloženo sudoku, které může hráč začít řešit.
    
    policka = odstran_pole(policka, policka, [], 0)
    prazdna_policka = []

    #Chceme projít všechna políčka a zapsat si ta, která jsou prázdná, jelikož s nimi bude moct uživatel pracovat narozdíl \
    #od políček vyplněných.
    for pole in policka:
        if pole.hodnota == None:
            prazdna_policka.append(pole)
            pole.je_prazdne = True

    return policka, prazdna_policka

#Nastavení barev:
ZELENA = (80,200,120)
CERNA = (0,0,0)
HNEDA = (193,154,107)
BILA = (255,255,255)
MODRA = (100,149,237)
SVETLE_ZLUTA = (255,255,51)
FIALOVA = (191,148,228)
CERVENA = (233,150,122)
ORANZOVA = (218,165,32)
ZLUTA = (255,255,0)
SVETLE_MODRA = (135,206,250)

class pole_s_textem:
    """Třída pro jakákoli místa na obrazovce, která v sobě budou mít text."""
    def __init__(self, napis, barva, font = ("Bookman Old Style", 80), je_sudoku = False, barva_textu = CERNA, \
        barva_okraje = CERNA):
        self.napis = napis
        self.barva = barva
        self.font_tlacitka = pygame.font.SysFont(font[0], font[1])
        self.barva_textu = barva_textu
        self.barva_okraje = barva_okraje
        #Tuto třídu, či její zděděnou třídu tlacitko budeme využívat pro tlačítka, místo na psaní vstupu a políčka v \
        #sudoku. Pro políčka v sudoku bude zobrazení fungovat o dost jinak, a proto si uložíme atribut je_sudoku, kterým \
        #rozpoznáme jak, chceme pole zobrazit.
        self.je_sudoku = je_sudoku

    def zobraz(self, okno, umisteni):
        """Funkce, která pole zobrazí na Surface - okno na danou pozici.
        umisteni: pro pole_s_textem, která nejsou políčka sudoku je to tuple, kde první element je střed umístění tlačítka 
        na ose x, druhý je střed umístění tlačítka na ose y. Pro políčka sudoku je to jen index políčka v seznamu všech
        políček, ze kterého zjistíme ve kterém sloupci a řádku sudoku se dané políčko nachází."""
        #Napíše nápis na Surface objekt text
        text = self.font_tlacitka.render(self.napis, False, self.barva_textu)
        
        #Pro tlačítka a prostor pro psaní vstupu využijeme širší okraj, fixní výšku, a šířku, která se bude odvíjet od \
        #délky textu.
        if self.je_sudoku == False:
            #Tyto rozměry sirka a vyska jsou rozměry celého prostoru. Chceme, aby prostor byl větší než text.
            sirka = text.get_width() + 40
            vyska = 120
            #prostor je Rect objekt, je to vyplnění.
            prostor = pygame.draw.rect(okno, self.barva, (umisteni[0] - sirka//2, umisteni[1] - vyska//2, sirka, vyska))
            #okraj je Rect objekt, tvoří okraj prostoru. Je lehce posunutý a větší než prostor, aby byl okraj vidět.
            okraj = pygame.draw.rect(okno, self.barva_okraje, (umisteni[0] - sirka//2 - 2, umisteni[1] - vyska//2 - 2, \
                sirka + 2, vyska + 2), 4)

            #text_rect je Rect objekt který zabírá stejnou velikost jako text a je umístěný uprostřed prostoru.
            text_rect = text.get_rect(center = prostor.center)
            #Text nakreslíme na obrazovku.
            okno.blit(text, text_rect)

        #Pro políčka sudoku využijeme danou výšku a šířku, užší okraj a u vepisování více možných hodnot i kontrolu, \
        #zda se vše vejde na řádek.
        else:
            #sirka a vyska jsou rozměry našeho políčka
            sirka = 70
            vyska = 70

            #Jelikož jsou v seznamu políčka uspořádaná po řádcích, umisteni%9 nám dá sloupec ve kterém se toto políčko \
            #nachází. 72 je šířka jednoho políčka + levého okraje. Pravý okraj chceme, aby se překrýval s levým okrajem \
            #tohoto políčka
            x = umisteni%9 * 72
            
            #umisteni//9 říká, ve kterém řádku se nacházíme.

            y = umisteni//9 * 72

            #Vnitřek políčka začne posunutý o 2, aby nechal prostor pro okraj. x, y jsou souřadnice okraje.
            tlacitko = pygame.draw.rect(okno, self.barva, (x + 2, y + 2, sirka, vyska))
            #Souřadnice okraje jsou x, y. Sirka, vyska je velikost vnitřku, takže ji musíme posunout.
            okraj = pygame.draw.rect(okno, self.barva_okraje, (x, y, sirka + 4, vyska + 4), 2)
            
            #Pokud zobrazujeme možné hodnoty a je jich víc než 5, tak se nevejdou na jeden řádek, a proto vytvoříme dva \
            #Rect objekty.
            if len(self.napis) > 9:
                text0 = self.font_tlacitka.render(self.napis[:9], False, self.barva_textu)
                text1 = self.font_tlacitka.render(self.napis[10:], False, self.barva_textu)

                text0_rect = text0.get_rect(center = (tlacitko.centerx, tlacitko.centery - 10))

                okno.blit(text0, text0_rect)
                text1_rect = text1.get_rect(center = (tlacitko.centerx, tlacitko.centery + 10))

                okno.blit(text1, text1_rect)

            else:
                text = self.font_tlacitka.render(self.napis, False, self.barva_textu)
                text_rect = text.get_rect(center = tlacitko.center)

                okno.blit(text, text_rect)

        #okraj je rect objekt, který je největší a zabírá plochu celého pole. Toto není důležité pro pole_s_textem, ale \
        #bude se to hodit pro zděděnou třídu tlacitko. Proto si tento okraj vrátíme.
        return okraj

class tlacitko(pole_s_textem):
    """Třída pro tlačítka, která budou pole_s_textem na která jde navíc i kliknout."""

    def __init__(self, napis, barva, font = ("Bookman Old Style", 80), je_sudoku = False, barva_textu = CERNA, \
        barva_okraje = CERNA):
        super().__init__(napis, barva, font, je_sudoku, barva_textu, barva_okraje)
        #Ukládáme si Rect objekt, který se nám bude hodit k detekování toho, zda na tlačítko bylo kliknuto. 
        self.rect = None

    def zobraz(self, okno, umisteni):
        """Funkce zobraz zobrazí tlačítko na okno na danou pozici stejně jako funkce zobraz třídy pole_s_textem. Zároveň
        si ale ještě do nového atributu rect uloží Rect objekt, který tlačítku odpovídá."""
        okraj = pole_s_textem.zobraz(self, okno, umisteni)
        #Ukládáme si Rect objekt, který se nám bude hodit k detekování toho, zda na tlačítko bylo kliknuto. 
        self.rect = okraj

    def bylo_zmacknuto(self, kurzor):
        """Funkce, která zkontroluje, zda je pozice kurzoru - předaná v proměnné kurzor - na tlačítku. Vrací False pokud
        ne a True pokud ano."""
        #V atributu self.rect je Rect objekt s pozicí na které byl naposled vykreslen.
        if self.rect.collidepoint(kurzor):
            return True
        else:
            return False

class prazdne_pole_sudoku(tlacitko):
    """Prázdná políčka v sudoku jsou také tlačítka. Je na ně potřeba umět kliknout. Chceme aby se políčka chovala trochu
    jinak než tlačítka, a proto jsme pro ně vytvořili speciální třídu."""
    def __init__(self, pole: policko):
        #Uložíme si příslušný objekt, abychom kdykoli měli přístup k jeho atributům.
        self.pole = pole
        self.barva = BILA
        self.je_sudoku = True
        self.barva_textu = MODRA
        font = ("Arial", 70)
        #Pokud uživatel do pole vepsal jednu hodnotu, chceme zobrazit tu.
        if pole.vepsana_hodnota != None:
            self.napis = pole.vepsana_hodnota
        #Pokud nemá vepsanou jednu hodnotu, ale má nějaké možnosti, tak chceme zobrazit ty.
        elif pole.vepsane_mozne_hodnoty != []:
            #Vytvoříme jeden textový řetězec ze všech čísel.
            self.napis = " ".join(cislo for cislo in pole.vepsane_mozne_hodnoty)
            #Pokud budeme zobrazovat vepsané možné hodnoty, chceme, aby byly vepsány menším písmem. Proto změníme font.
            font = ("Arial", 20)
        #Pokud o poli nemá poznamenáno nic, tak se zobrazí prázdné.
        else:
            self.napis = ""
        super().__init__(self.napis, self.barva, font, self.je_sudoku, self.barva_textu)

def hra():
    """Funkce, která spustí celou hru. Dokud běží program, tak běží hra."""
    
    def zkontroluj_pocet_policek(vstup):
        """Funkce, která zkontroluje zda počet políček zadaný uživatelem je vhodný. Jako první argument vrací vysledek - 
        False, pokud vstup vhodný není, True pokud je. Druhý argument je zprava, která se uživateli zobrazí."""
        znat = vstup
        try:
            znat = int(znat)
            if znat < 17:
                zprava = "Sudoku s méně než 17 odhalenými číslicemi nikdy nebude mít pouze jedno řešení. Musíte zadat větší číslo."
                vysledek = False
            elif znat > 81:
                zprava = "Tolik číslic v sudoku není."
                vysledek = False
            #Jelikož používáme elif, znamená to, že znat je větší nebo rovno 17, ale menší než 26. 
            elif znat < 26:
                zprava = "I když sudoku mohou mít takový počet číslic, není takových sudoku mnoho a jejich nalezení by mohlo trvat příliš dlouho. Zadejte prosím větší číslo."
                vysledek = False
            else:
                zprava = "Děkujeme. Vaše sudoku se právě generuje."
                vysledek = True
        except ValueError:
            zprava = "Musíte zadat číslo."
            vysledek = False
        return vysledek, zprava

    def zobraz_text(okno, text, pozice):
        """Funkce, která zobrazí text na obrazovku tak, aby se podle potřeby rozložil do řádků.
        okno: Surface na který zobrazujeme
        text: text, který zobrazujeme
        pozice: pozice na které se začne text zobrazovat"""

        font_text = pygame.font.SysFont("Bookman Old Style", 60)

        #Chceme text rozdělovat po slovech. Vytvoříme si seznam slova, ve kterém každý prvek odpovídá jednomu slovu v textu.
        slova = text.split() 

        #V proměnné mezera si uložíme šířku mezery, to bude důležité pro upravování pozice.
        mezera = font_text.size(" ")[0]        
        #V proměnné max_sirka si uložíme šířku obrazovky, která nám říká jaké max hodnoty může nabývat x souřadnice.
        max_sirka = okno.get_size()[0]

        #Souřadnice x, y se budou neustále měnit, jak budeme psát jednotlivá slova.
        x, y = pozice

        for slovo in slova:
            #Vytvoříme Surface objekt s textem. To nám umožní zjistit o něm informace a následně ho nakreslit na obrazovku. 
            slovo_surf = font_text.render(slovo, False, CERNA)
            #Zjistíme jeho velikost, ta nám pomůže zjistit o kolik máme posunout souřadnice x a y.
            sirka_slova, vyska_slova = slovo_surf.get_size()
            #Pokud už se toto slovo na současný řádek nevejde. Chceme ho napsat na začátek nového řádku. Tzn. resetovat \
            #souřadnici x a zvětšit souřadnici y o výšku slova.
            if x + sirka_slova >= max_sirka:
                x = pozice[0]
                y += vyska_slova
            okno.blit(slovo_surf, (x,y))
            #Jelikož jsme slovo napsali, musíme k souřadnici x připočíst jeho délku a délku jedné mezery, kterou bychom \
            #za slovo jakoby napsali. 
            x += sirka_slova + mezera

    #Při spuštění programu je program zapnutý. Okno hry bude zapnuto a aktualizováno, dokud bude program běžet.
    zapnuto = True

    #Pokud je priprava True, tak jsme ve fázi, že hra chce od uživatele zjistit kolik chce v sudoku znát číslic. Na \
    #začátku jsme v hlavním menu, a proto je toto False.
    priprava = False

    #Pokud je reseni True, tak jsme ve fázi, kdy uživatel může řešit sudoku. Na začátku je toto False.
    reseni = False

    #Inicializuje pygame moduly.
    pygame.init()

    #Nastaví velikost okna na velikost monitoru. 
    info_objekt = pygame.display.Info()
    sirka_obrazovky, vyska_obrazovky = info_objekt.current_w, info_objekt.current_h
    okno = pygame.display.set_mode((sirka_obrazovky, vyska_obrazovky))
    
    #Získáme informace o prostředku obrazovky pro pozicování aspektů. 
    prostredek_x = okno.get_rect().centerx
    prostredek_y = okno.get_rect().centery

    while zapnuto == True:

        #Neustále kontrolujeme jestli nebylo něco zmáčknuto.
        for event in pygame.event.get():
            #Pokud bylo zmáčknuté levé tlačítko myši, chceme zkontrolovat kde se nachází kurzor a zda bylo zmáčknuto \
            #některé tlačítko.            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    kurzor = pygame.mouse.get_pos()
                    #Pokud bylo zmáčnuto tlačítko ukoncit, chceme celý program ukončit. Toho dosáhneme změněním hodnoty \
                    #zapnuto, čímž skončí hlavní while cyklus.
                    vypnout = ukoncit.bylo_zmacknuto(kurzor)
                    if vypnout == True:
                        zapnuto = False
                    #Pokud bylo zmáčknuto tlačítko nove, chceme spustit druhou fázi, kdy se program ptá uživatele na počet \
                    #číslic. To naznačíme změnou hodnoty priprava na True.
                    generovat = nove.bylo_zmacknuto(kurzor)
                    if generovat == True:
                        priprava = True

        #Vybarví celé okno světle hnědou barvou.
        okno.fill(HNEDA)

        #Zobrazí hlavní nadpis
        font_nadpis = pygame.font.SysFont("Harrington", 200)
        nazev = font_nadpis.render("SUDOKU", False, CERNA)
        okno.blit(nazev, nazev.get_rect(centerx = prostredek_x, centery = vyska_obrazovky//5))
        
        nove = tlacitko("Nové sudoku", ZELENA)
        nove.zobraz(okno, (prostredek_x, vyska_obrazovky//2))    
        ukoncit = tlacitko("Ukončit program", ZELENA)
        ukoncit.zobraz(okno, (prostredek_x, 3*vyska_obrazovky//4))

        #Zobrazí všechny změny.
        pygame.display.flip()
        
        #V proměnné vstup je vše, co zatím uživatel zadal. Na začátku je to nic.
        vstup = ""
        
        #Pokud jsme ve fázi priprava, tak chceme zde uživatele držet dokud nám nezadá platný počet číslic, které chce znát.
        while priprava == True:

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        kurzor = pygame.mouse.get_pos()
                        vypnout = ukoncit.bylo_zmacknuto(kurzor)
                        if vypnout == True:
                            #Pokud bylo zmáčknuto tlačítko ukoncit, chceme vypnout celý program, proto musíme nejprve \
                            #ukončit aktuální fázi přípravy.
                            priprava = False
                            zapnuto = False
                
                #Pokud bylo zmáčknuto tlačítko na klávesnici, zvlášť nás zajímá stisknutí klávesy backspace, \
                #kterou se bude vstup vymazávat, a klávesy enter, kterou se vstup bude potvrzovat. Zbytek kláves \
                #převedeme na textový řetězec.
                elif event.type == pygame.KEYDOWN:
                    #Pokud uživatel stiskl enter, chceme odeslat vstup na zkontrolování funkci zkontroluj_pocet_policek.
                    if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                        vysledek, zprava = zkontroluj_pocet_policek(vstup)

                        #Pokud vstup nebyl vhodný pokračujeme v této fázi a resetujeme vstup.                        
                        if vysledek == False:
                            
                            #Nejprve chceme uživateli ukázat zprávu. Zpráva se bude zobrazovat, dokud uživatel neklikne \
                            #na tlačítko ok, enter, nebo program nevypne.
                            koukame_na_zpravu = True
                            while koukame_na_zpravu == True:

                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        if event.button == 1:
                                            kurzor = pygame.mouse.get_pos()
                                            vypnout = ukoncit.bylo_zmacknuto(kurzor)
                                            if vypnout == True:
                                                #Pokud bylo zmáčknuto tlačítko ukoncit, chceme vypnout celý program, proto musíme \
                                                #nejprve ukončit koukání na zprávu, fázi přípravy a celý program.
                                                koukame_na_zpravu = False
                                                priprava = False
                                                zapnuto = False
                                            #Pokud uživatel kliknul na tlačítko ok, chceme se vrátit zpět k vepisování vstupu.
                                            odkliknuto = ok.bylo_zmacknuto(kurzor)
                                            if odkliknuto == True:
                                                koukame_na_zpravu = False
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                                            koukame_na_zpravu = False

                                okno.fill(HNEDA)
                                zobraz_text(okno, zprava, (20,20))

                                ok = tlacitko("OK", ZELENA)
                                ok.zobraz(okno, (prostredek_x, prostredek_y))

                                ukoncit.zobraz(okno, (prostredek_x, 4*vyska_obrazovky//5))

                                pygame.display.flip()

                            #Jakmile uživatel odkliknul zprávu, vracíme se zpět, opět s prázdným vstupem.
                            vstup = ""

                        #Pokud byl vstup vhodný můžeme sudoku vygenerovat.
                        else:
                            #Nejprve chceme zobrazit zprávu. Ta se bude ukazovat po celou dobu generování sudoku.
                            okno.fill(HNEDA)
                            zobraz_text(okno, zprava, (20,20))
                            ukoncit.zobraz(okno, (prostredek_x, 4*vyska_obrazovky//5))
                            pygame.display.flip()

                            #Vygenerujeme sudoku podle požadavků. Číslo je uloženo jako string v proměnné vstup.
                            policka, prazdna_policka = vygeneruj_sudoku(int(vstup))

                            #Jakmile sudoku vygenerujeme, chceme ukončit fázi přípravy a začít fázi řešení.
                            priprava = False
                            reseni = True

                    #Pokud uživatel stiskl backspace, chceme odstranit ze vstupu poslední znak.
                    elif event.key == pygame.K_BACKSPACE:
                        vstup = vstup[:-1]
                    else:
                        vstup += event.unicode

            okno.fill(HNEDA)

            instrukce = "Kolik si přejete aby v sudoku bylo vyplněných polí? Zadej číslo od 26 do 81. Číslo napište číslicemi. Vstup potvrďte klávesou enter. Svůj vstup můžete vymazat klávesou backspace."
            zobraz_text(okno, instrukce, (20,20))

            #prostor_pro_uzivatele je okénko ve kterém se bude zobrazovat vše, co uživatel napíše. 
            prostor_pro_uzivatele = pole_s_textem(vstup, HNEDA)
            prostor_pro_uzivatele.zobraz(okno, (prostredek_x, 6*vyska_obrazovky//11))

            ukoncit.zobraz(okno, (prostredek_x, 4*vyska_obrazovky//5))
            
            pygame.display.flip()
        
        #Pokud jsme ve fázi řešení, tak zde zůstaneme dokud uživatel program neukončí, nebo si nenechá vygenerovat nové \
        #sudoku.

        #Proměnná aktivni_policko nám říká s kterým políčkem chce uživatel právě pracovat, na začátku to není žádné.
        aktivni_policko = None

        #Ve fázi řešení jsou tři hlavní módy, psaní hodnot, psaní možností, a vymazávání. Ve kterém módu se nacházíme \
        #bude uloženo v proměnné mod. Bude nabývat hodnot 1-3, které po řadě odpovídají jednotlivým módům. Na začátku \
        #je spuštěn mód vpisování hodnot.
        mod = 1

        #Krom tří různých módu, také může být zapnutý nebo vypnutý mód kontroly, který kontroluje vepsané hodnoty, a \
        #zvýrazňuje ty špatné. Tento mód je automaticky vypnutý.
        kontrolovat = False

        while reseni == True:
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        kurzor = pygame.mouse.get_pos()
                        vypnout = ukoncit.bylo_zmacknuto(kurzor)
                        if vypnout == True:
                            #Pokud bylo zmáčknuto tlačítko ukoncit, chceme vypnout celý program, proto musíme nejprve \
                            #ukončit aktuální fázi řešení.
                            reseni = False
                            zapnuto = False
                        #Pokud bylo zmáčknuto tlačítko generovat, chceme se vrátit zpět do fáze přípravy. Proto musíme \
                        #nejprve ukončit fázi řešení.
                        generovat = nove.bylo_zmacknuto(kurzor)
                        #Zkontrolujeme, jestli bylo zmáčknuto některé tlačítko módů.
                        if generovat == True:
                            reseni = False
                            priprava = True
                        mod_1 = vepsat.bylo_zmacknuto(kurzor)
                        if mod_1 == True:
                            mod = 1
                        mod_2 = poznamky.bylo_zmacknuto(kurzor)
                        if mod_2 == True:
                            mod = 2
                        mod_3 = vymazat.bylo_zmacknuto(kurzor)
                        if mod_3 == True:
                            mod = 3
                        #Dále zkontrolujeme jestli byla zmáčknuta kontrola. Pokud ano, tak chceme změnit hodnotu \
                        #kontrolovat. Toho dosáhneme logickou operací not.
                        prepnout = kontrola.bylo_zmacknuto(kurzor)
                        if prepnout == True:
                            kontrolovat = not(kontrolovat)
                        #Musíme zkontrolovat všechna prázdná pole, jestli nebylo kliknuto na ně.
                        #Pozice políček sudoku je v nich uložena relativně vůči tabulce, která je ale na obrazovce posunutá \
                        #o 20 pixelů dolů a doprava, proto musíme upravit i pozici kurzoru.
                        kurzor = (kurzor[0] - 20, kurzor[1] - 20)
                        for pole in prazdna_policka:
                            pozice = policka.index(pole)
                            kliknuto = pole.pole_sudoku.bylo_zmacknuto(kurzor)
                            if kliknuto == True:
                                aktivni_policko = pole.aktivni(aktivni_policko)
                                #Už jsme našli místo, kde bylo kliknuto, a tedy nemusíme prozkoumávat ostatní pole.
                                break
                
                if event.type == pygame.KEYDOWN:
                    #Jakékoli klávesy nás zajímají pouze pokud máme nějaké zvolené aktivní políčko.abs
                    if aktivni_policko != None:
                        #Pokud jsme v módu mazání, zajímá nás pouze stisknutí klávesy backspace nebo delete
                        if mod == 3:
                            #Pokud byl stisknuto backspace nebo delete, tak chceme smazat hodnotu v aktivním políčku.
                            if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                                aktivni_policko.vepsana_hodnota = None
                        #Pokud nejsme v módu mazání, tak chceme zjistit jestli uživatel zadal číslo.
                        zmacknuto = event.unicode
                        #Pokud ano, postup se bude lišit pro mód vpisování hodnoty a mód vpisování možných hodnot.
                        if zmacknuto in "123456789":
                            #U 1. módu jednoduše zapíšeme hodnotu.
                            if mod == 1:
                                aktivni_policko.vepsana_hodnota = zmacknuto
                            #U druhého zkontroujeme zda daná hodnota je v seznamu možných hodnot, v takovém případě \
                            #ji odstraníme. Pokud tam není, tak ji tam přidáme.
                            elif mod == 2:
                                if zmacknuto in aktivni_policko.vepsane_mozne_hodnoty:
                                    aktivni_policko.vepsane_mozne_hodnoty = odstran_hodnotu_ze_seznamu(
                                        aktivni_policko.vepsane_mozne_hodnoty, zmacknuto)
                                else:
                                    aktivni_policko.vepsane_mozne_hodnoty.append(zmacknuto)

            okno.fill(HNEDA)
            
            #Vytvoříme si surface pro sudoku tabulku. Na ní si uspořádáme políčka a pak jen celou tabulku umístíme na \
            #obrazovku. To nám umožní pozicovat políčka od (0,0).
            tabulka = pygame.Surface((650,650))

            #Všechna políčka zobrazíme na tabulku.
            for i in range(81):
                pole = policka[i]
                #Pokud je pole vyplněné, uživatel do něj psát nemůže. Nebude to tedy vůbec tlačítko, ale pole s textem.
                if pole.je_prazdne == False:
                    pole_sudoku = pole_s_textem(pole.hodnota, BILA, font=("Arial", 70), je_sudoku = True)
                #Pokud je pole prázdné, chceme, aby pole bylo tlačítko, dalo se na něj klikat a psát do něj. 
                else:
                    pole_sudoku = prazdne_pole_sudoku(pole)
                    #Uložíme si objekt pole_sudoku do atributu políčka, abychom k němu mohli mít i nadále přístup.
                    pole.pole_sudoku = pole_sudoku    
                #Jelikož jde o sudoku stačí jako argument umístění uvést jen pořadí políčka.
                pole_sudoku.zobraz(tabulka, i)

            #Pokud máme nějaké políčko zvýrazněné, musíme jeho pozadí přebarvit na žlutou.
            if aktivni_policko != None:
                index_pole = policka.index(aktivni_policko)
                aktivni_policko.pole_sudoku.barva = SVETLE_ZLUTA
                aktivni_policko.pole_sudoku.zobraz(tabulka, index_pole)

            #Nakreslíme silnější okraje mezi čtverci 3*3.
            for i in range(4):
                pygame.draw.line(tabulka, CERNA, (i*216, 0), (i*216, 650), 4)
                pygame.draw.line(tabulka, CERNA, (0, i*216), (650, i*216), 4)

            okno.blit(tabulka, (20,20))

            vepsat = tlacitko("Vepsat hodnotu", SVETLE_MODRA)
            poznamky = tlacitko("Vepsat možnosti", FIALOVA)
            vymazat = tlacitko("Vymazat hodnotu", CERVENA)

            #Podle toho ve kterém jsme módu, se danému tlačítku zvýrazní text a okraj.
            if mod == 1:
                aktivni_mod = vepsat
            elif mod == 2:
                aktivni_mod = poznamky
            else:
                aktivni_mod = vymazat
            aktivni_mod.barva_okraje = ZLUTA
            aktivni_mod.barva_textu = ZLUTA

            vepsat.zobraz(okno, (3*sirka_obrazovky//4, vyska_obrazovky//7))
            poznamky.zobraz(okno, (3*sirka_obrazovky//4, 1*vyska_obrazovky//3))
            vymazat.zobraz(okno, (3*sirka_obrazovky//4, 8*vyska_obrazovky//15))

            #Text v tlačítku kontroly bude jiný pokud bude kontrola zapnutá nebo vypnutá.
            if kontrolovat == False:
                kontrola = tlacitko("Kontrola: OFF", ORANZOVA)
            else:
                kontrola = tlacitko("Kontrola: ON", ORANZOVA)
            kontrola.zobraz(okno, (3*sirka_obrazovky//4, 5*vyska_obrazovky//7))


            #Zobrazíme tlačítka pro vygenerování nového sudoku a vypnutí programu.
            nove.zobraz(okno, (sirka_obrazovky/5, 8*vyska_obrazovky//9))
            ukoncit.zobraz(okno, (3*sirka_obrazovky//4, 8*vyska_obrazovky//9))

            pygame.display.flip()


hra()
