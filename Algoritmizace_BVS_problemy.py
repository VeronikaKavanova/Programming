class VrcholBinStromu:
    """třída pro reprezentaci vrcholu binárního stromu""" 
    def __init__(self, info = None, levy = None, pravy = None):
        self.info = info      # data
        self.levy = levy      # levé dítě 
        self.pravy = pravy    # pravé dítě


def Naslednik(koren, k):
    
    bez_naslednik = None

    def naslednik(koren, k):
        nonlocal bez_naslednik
        if k >= koren.info:
            if koren.pravy != None:
                naslednik(koren.pravy, k)
        else:
            if bez_naslednik == None or koren.info < bez_naslednik:
                bez_naslednik = koren.info
            if koren.levy != None:
                naslednik(koren.levy, k)

    naslednik(koren, k)

    return bez_naslednik

def Predchuzce(koren, k):
    
    bez_predchuzce = None

    def predchuzce(koren, k):
        nonlocal bez_predchuzce
        if k <= koren.info:
            if koren.levy != None:
                predchuzce(koren.levy, k)
        else:
            if bez_predchuzce == None or koren.info > bez_predchuzce:
                bez_predchuzce = koren.info
            if koren.pravy != None:
                predchuzce(koren.pravy, k)

    predchuzce(koren, k)

    return bez_predchuzce

def Uloz(koren, klic):
    while koren != None:
        if klic < koren.info:
            koren = koren.levy
        elif klic > koren.info:
            koren = koren.pravy
        else: #klíč už ve stromě je
            return koren
    koren = VrcholBinStromu(klic)

def Vymaz(koren, klic):
    
    def vyhledej(vrchol, klic):
        if klic == vrchol.levy.info:
            return vrchol, vrchol.levy, "l"
        elif klic == vrchol.pravy.info:
            return vrchol, vrchol.pravy, "p"
        if klic < vrchol.info:
            return vyhledej(vrchol.levy, klic)
        else:
            return vyhledej(vrchol.pravy, klic)

    rodic, vrchol, strana = vyhledej(koren, klic)
    if vrchol.levy == None and vrchol.pravy == None:
        if strana == "l":
            rodic.levy = None
        else:
            rodic.pravy = None
    elif vrchol.levy == None:
        if strana == "l":
            rodic.levy = vrchol.pravy
        else:
            rodic.pravy = vrchol.pravy
    elif vrchol.pravy == None:
        if strana == "l":
            rodic.levy = vrchol.levy
        else:
            rodic.pravy = vrchol.levy
    else:
        naslednik = vrchol.pravy
        while naslednik.levy != None:
            naslednik = naslednik.levy
        Vymaz(vrchol, naslednik)
        naslednik.levy, naslednik.pravy = vrchol.levy, vrchol.pravy
        if strana == "l":
            rodic.levy = naslednik
        else:
            rodic.pravy = naslednik

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

Vymaz(v1, 6)

def projdi(vrchol):
    print(vrchol.info)
    if vrchol.levy != None:
        projdi(vrchol.levy)
    if vrchol.pravy != None:
        projdi(vrchol.pravy)

projdi(v1)