class VrcholBinStromu:
    def __init__(self, info=None, levy=None, pravy=None):
        self.info = info
        self.levy = levy
        self.pravy = pravy

def podstrom(koren: VrcholBinStromu, x: int):
    """
    koren: kořen zadaného binárního stromu
    x: celé číslo
    vrátí: seznam čísel uložených ve všech vrcholech, které leží v podstromu s kořenem obsahujícím číslo x
    předpokládá, že x se ve stromu nachází
    """

    #nejprve vyhledáme vrchol s číslem x, jelikož se jedná o binární strom a ne BVS, tj. o vrcholech neznáme žádné
    #informace, tak budeme muset procházet celý strom, dokud na x nenarazíme

    def vyhledej(koren, x):
        """vrátí vrchol s hodnotou x"""
        if koren.info == x:
            #pokud jsme nalezli hledany vrchol, tak ho vratime
            return koren
        if koren.levy != None:
            #chceme rekurzivně prohledat levý podstrom, pokud existuje
            vysledek = vyhledej(koren.levy, x)
            #pokud vrchol najdeme, potřebujeme ho vrátit skrze všechny rekurzivní volání
            if vysledek != None:
                return vysledek
        if koren.pravy != None:
            vysledek = vyhledej(koren.pravy, x)
            if vysledek != None:
                return vysledek

    def seznam(koren):
        """vrátí seznam všech vrcholů podstromu s kořenem koren. Strom prochází metodou DFS preorder"""
        #je třeba jen celý podstrom projít
        hodnoty = []

        def seznam_rek(koren):
            """rekurzivní část procházení stromem pomocí DFS preorder. Je oddělená kvůli zachování seznamu."""
            nonlocal hodnoty
            hodnoty.append(koren.info)
            if koren.levy != None:
                seznam_rek(koren.levy)
            if koren.pravy != None:
                seznam_rek(koren.pravy)
        
        seznam_rek(koren)
        return(hodnoty)

    koren_podstromu = vyhledej(koren, x)
    hodnoty = seznam(koren_podstromu)
    return hodnoty

v1 = VrcholBinStromu(8)
v2 = VrcholBinStromu(3)
v3 = VrcholBinStromu(10)
v4 = VrcholBinStromu(1)
v5 = VrcholBinStromu(5)
v6 = VrcholBinStromu(14)
v7 = VrcholBinStromu(4)
v8 = VrcholBinStromu(6)
v9 = VrcholBinStromu(13)

v1.levy, v1.pravy = v2, v3
v2.levy, v2.pravy = v4, v5
v3.pravy = v6
v5.levy, v5.pravy = v7, v8
v6.levy = v9

print(podstrom(v1, 20))