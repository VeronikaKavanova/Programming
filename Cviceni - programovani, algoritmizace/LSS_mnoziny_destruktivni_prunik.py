class Prvek:
    def __init__(self, x, dalsi):
        self.x = x
        self.dalsi = dalsi

def VytiskniLSS( p ):
    print( "LSS:", end=" " )
    while p!=None:
        print( p.x, end=" " )
        p = p.dalsi
    print(".")

def NactiLSS():
    """cte cisla z radku, dokud nenacte prazdny radek"""
    prvni = None
    posledni = None
    r = input()
    while r!="":
        radek = r.split()
        if len(radek)==0: # protoze ten test r!="" v RCDX neukoncil cyklus!
            break
        for s in radek:
            p = Prvek(int(s),None)
            if prvni==None:
                prvni = p
            else:
                posledni.dalsi = p
            posledni = p
        r = input()
    return prvni

#################################################

def IntersectionDestruct(a,b):
    """ destruktivni prunik dvou usporadanych seznamu
    * nevytvari zadne nove prvky, vysledny seznam bude poskladany z prvku puvodnich seznamu,
    * vysledek je MNOZINA, takze se hodnoty neopakuji """

    # sem doplnte kod funkce, dalsi casti zdrojoveho kodu NEMENTE

    #pokud je jeden ze seznamů prázdný, tak je prázdný průnik
    if a == None or b == None:
        return None
    #nejprve musime najit nejmensi prvek, postupujeme tak dlouho, dokud nejaky nenajdeme
    #nebo dokud nedojdeme na konec jednoho ze seznamu
    nejmensi = None
    while nejmensi == None and a != None and b != None:
        if a.x == b.x:
            nejmensi = a 
            a = a.dalsi
            b = b.dalsi
        #pokud nejsou stejne, tak ten menší už určitě nebude v druhém seznamu, takže se posuneme na další prvek
        elif a.x < b.x:
            a = a.dalsi
        else:
            b = b.dalsi

    #prvky ma smysl porovnavat od nejmensich, ale odkazy se musi menit odzadu jinak bychom ztratili zbytek seznamu,
    #vytvorime si pomocne atributy, novy_dalsi, kterym, az bude cas, nahradime dalsi,
    #a predchozi, abychom mohli seznamem postupovat i zpet

    if nejmensi != None:
        nejmensi.predchozi = None 
    else:
        return None #pokud jsme nenasli zadny spolecny prvek, průnik je prázdný

    #postupujeme stejně jako předtím. Opět pouze do okamžiku, kdy jeden seznam nedojde na konec
    while a != None and b != None:
        #ne vzdy najdeme dalsi prvek, na zacatku kazde iterace ho nastavime na None
        #to nam umozni provadet podminky v pripade, ze se z None zmeni na neco jineho
        druhy_mensi = None
        if a.x == b.x:
            druhy_mensi = a
            a = a.dalsi
            b = b.dalsi
        elif a.x < b.x:
            a = a.dalsi
        else:
            b = b.dalsi

        if druhy_mensi != None:
            #nejmenší v průniku bude odkazovat na prvek hned za sebou
            nejmensi.novy_dalsi = druhy_mensi
            druhy_mensi.predchozi = nejmensi
            #druhý nejmenší prvek se teď stává nejmenším
            nejmensi = druhy_mensi

    #v prvku nejmensi ted mame uložený poslední prvek 

    #ted postupne odzadu updatujeme vsechny odkazy dalsi na novy_dalsi

    #poslední prvek nemá žádný odkaz novy_dalsi, tak mu ho vyrobíme
    nejmensi.novy_dalsi = None

    while nejmensi.predchozi != None:
        nejmensi.dalsi = nejmensi.novy_dalsi
        nejmensi = nejmensi.predchozi
    #uplne prvni prvek jsme ještě neupdatovali
    nejmensi.dalsi = nejmensi.novy_dalsi
    
    return nejmensi

#################################################

VytiskniLSS( IntersectionDestruct( NactiLSS(), NactiLSS() ) )
