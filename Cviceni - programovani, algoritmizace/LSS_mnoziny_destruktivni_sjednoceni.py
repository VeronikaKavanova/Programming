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

def UnionDestruct(a,b):
    """ destruktivni prunik dvou usporadanych seznamu
    * nevytvari zadne nove prvky, vysledny seznam bude poskladany z prvku puvodnich seznamu,
    * vysledek je MNOZINA, takze se hodnoty neopakuji """

    # sem doplnte kod funkce, dalsi casti zdrojoveho kodu NEMENTE

    #funkce nacte prvni prvky obou seznamu
    #porovname je, ten mensi oznacime a presuneme se na dalsi prvek v jeho seznamu
    
    if a != None and b!= None:
        if a.x < b.x:
            nejmensi = a
            a = a.dalsi
        elif a.x == b.x:
            #pokud jsou stejne, chceme tento prvek jednou oznacit a v obou seznamech se posunout dal
            nejmensi = a
            a = a.dalsi
            b = b.dalsi
        else:
            nejmensi = b
            b = b.dalsi

    #prvky ma smysl porovnavat od nejmensich, ale odkazy se musi menit odzadu jinak bychom ztratili zbytek seznamu,
    #vytvorime si pomocne atributy, novy_dalsi, kterym, az bude cas, nahradime dalsi,
    #a predchozi, abychom mohli seznamem postupovat i zpet
    
    elif a != None:
        nejmensi = a
        a = a.dalsi
    elif b != None:
        nejmensi = b
        b = b.dalsi
    else:
        return None
    
    nejmensi.predchozi = None
    
    while a != None and b != None:
        if a.x < b.x:
            druhy_mensi = a
            a = a.dalsi
        elif a.x == b.x:
            druhy_mensi = a
            a = a.dalsi
            b = b.dalsi
        else:
            druhy_mensi = b
            b = b.dalsi

        nejmensi.novy_dalsi = druhy_mensi
        druhy_mensi.predchozi = nejmensi
        nejmensi = druhy_mensi

    #cyklus skonci jakmile nektery seznam dojde na konec, posledni prvek z tohoto seznamu je nejmensi,
    #musime za nej pripojit zbytek druheho seznamu
    if a != None:
        zbytek = a
    else:
        zbytek = b

    #zbytek uz funguje, je z jednoho seznamu, ktery uz byl ve spravnem tvaru, musime ho jen napojit na posledni prvek
    nejmensi.novy_dalsi = zbytek
    #ted postupne odzadu updatujeme vsechny odkazy
    while nejmensi.predchozi != None:
        nejmensi.dalsi = nejmensi.novy_dalsi
        nejmensi = nejmensi.predchozi
    nejmensi.dalsi = nejmensi.novy_dalsi
    
    return nejmensi
#################################################

VytiskniLSS( UnionDestruct( NactiLSS(), NactiLSS() ) )
