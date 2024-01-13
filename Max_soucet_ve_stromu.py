class VrcholBinStromu:
    """třída pro reprezentaci vrcholu binárního stromu""" 
    def __init__(self, info = None, levy = None, pravy = None):
        self.info = info      # data
        self.levy = levy      # levé dítě 
        self.pravy = pravy    # pravé dítě
                
def maxcena(koren : VrcholBinStromu):
    """
    koren : kořen zadaného binárního stromu
    vrátí : dvojici čísel (m,d), kde m je maximální součet čísel na cestě z kořenu do libovolného vrcholu stromu a
            a d je délka této cesty (je-li jich více, tak nejkratší)
    """

    """
    do každého vrcholu vede unikátní cesta, tzn. každý vrchol má svůj součet, který získáme kdybychom ho \
        vybrali jako vrchol ve kterém chceme skončit. Musíme projít všechny vrcholy a zjistit ve kterém \
            je největší součet.
    """

    #max_soucet budeme updatovat vždy když najdeme vrchol s větším součtem. Na začátku je to prostě že zůstaneme\
    # v kořeni. Druhá položka je počet hran, kterými musíme projít, abychom tohoto součtu dosáhli.
    max_soucet = [koren.info, 0]

    def maxsoucet(koren: VrcholBinStromu, soucet, cesta):
        """rekurzivní funkce, která prochází vrcholy stromu, sčítá součet nacestě a pokud narazí na větší možný \
            maximální součet nebo kratší cestu, jak ho dosáhnout upraví nelokální proměnnou max_soucet
        koren: kořen podstromu, který kontrolujeme
        soucet: součet v rodiči kořene podstromu
        cesta: délka cesty do kořene podstromu"""

        nonlocal max_soucet #potřebujeme upravovat max_soucet, pokud najdeme větší

        koren.soucet = koren.info + soucet 
        #uložíme součet v kořeni, který je roven součtu na cestě do kořene + hodnota v kořeni

        if koren.soucet > max_soucet[0]:
            max_soucet = [koren.soucet, cesta]
        elif koren.soucet == max_soucet[0] and cesta < max_soucet[1]:
            max_soucet[1] = cesta
        
        if koren.levy != None:
            maxsoucet(koren.levy, koren.soucet, cesta+1)
        if koren.pravy != None:
            maxsoucet(koren.pravy, koren.soucet, cesta+1)
    
    maxsoucet(koren, 0, 0)
    print(max_soucet)

v1 = VrcholBinStromu(314)
v2 = VrcholBinStromu(-6)
v3 = VrcholBinStromu(6)
v4 = VrcholBinStromu(271)
v5 = VrcholBinStromu(2)
v6 = VrcholBinStromu(40)
v7 = VrcholBinStromu(30)

v1.levy, v1.pravy = v2, v3
v2.levy = v4
v3.levy, v3.pravy = v5, v6
v5.pravy = v7

maxcena(v1)