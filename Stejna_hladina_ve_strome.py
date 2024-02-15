class VrcholBinStromu:
    """třída pro reprezentaci vrcholu binárního stromu""" 
    def __init__(self, info = None, levy = None, pravy = None):
        self.info = info      # data
        self.levy = levy      # levé dítě 
        self.pravy = pravy    # pravé dítě

def hladina(koren : VrcholBinStromu, x : int):
    """
    koren : kořen zadaného binárního stromu
    x     : zadané ohodnocení hledaného vrcholu
    vrátí : seznam čísel vrcholů na hladině obsahující x
    """

    def najdi_hladinu():
        #jelikož hledáme vrcholy na stejné hladině, bude se nám hodit algoritmus průchodem do šířky, 
        #který strom prochází po hladinách. Ale jelikož budeme chtít poté celou hladinu vrátit, nebudeme do fronty
        #ukládat přímo vrcholy, ale uložíme do ní pole se všemi vrcholy na té hladině. 

        #jelikož ve frontě bude vždy v jednom prvku celá hladina, najednou potřebujeme ve frontě pouze dva prvky
        # - současnou hladinu a hladinu příští. Z toho důvodu ani nepotřebujeme vytvářet frontu, ale uložíme si
        #hladiny do proměnných

        soucasna = [koren]

        #provádíme cyklus dokud máme na hladině nějaké vrcholy
        while soucasna != []:
            pristi = [None]*(2*len(soucasna)) #každý vrchol ze současné hladiny má nanejvýš dvě děti,
            #tudíž si můžeme připravit pole správné velikosti
            zacatek = 0 #kam máme do pole pristi ukladat další vrchol
            for vrchol in soucasna:
                if vrchol.info == x: 
                    #pokud jsme našli vrchol x, tak se nachází v této hladině, a tudíž ji celou můžeme vrátit
                    return soucasna
                #do příští hladiny si uložíme děti tohoto vrcholu. Takto se tam uloží všechny děti všech vrcholů
                #na této hladině
                if vrchol.levy != None:
                    pristi[zacatek] = vrchol.levy
                    zacatek += 1
                if vrchol.pravy != None:
                    pristi[zacatek] = vrchol.pravy
                    zacatek += 1
            #jakmile jsme prošli všechny vrcholy na této hladině, přesouváme se na další
            if pristi != [None]*(2*len(soucasna)):
                soucasna = pristi[:zacatek] #na konci pristi jsou None, pokud nebyl strom plně zaplněn, 
                    #chceme vrátit jen skutečně zaplněná místa
            else:
                #pokud už v další hladině žádné vrcholy nejsou, tak to znamená, že jsme vrchol s hodnotou x nenašli
                return []

    def hodnoty(hladina):
        """vrátí seznam hodnot ve vrcholech v dané hladině"""
        cisla = [None]*len(hladina)
        zacatek = 0
        for vrchol in hladina:
            cisla[zacatek] = vrchol.info
            zacatek += 1
        return cisla[:zacatek] #chceme vrátit jen skutečně využitý prostor
    
    Hladina = najdi_hladinu()
    Hodnoty = hodnoty(Hladina)
    return Hodnoty

binstrom = VrcholBinStromu(1,
             VrcholBinStromu(2,VrcholBinStromu(4)),              
             VrcholBinStromu(3,
                 VrcholBinStromu(5,None,VrcholBinStromu(7)),
                 VrcholBinStromu(6)))
print(hladina(binstrom, 4))