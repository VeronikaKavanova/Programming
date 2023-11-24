class ZasbonikPole:
    def __init__(self):
        self.pole = [] #prázdný zásobník
    def push(self,x): #vloží x
        self.pole.append(x)
    def pop(self): #odebere vrchol
        #předpokládá neprázdný zásobník, při nesplnění je vhodné vyvolat výjimku
        return self.pole.pop()

class FrontaPole:
    def __init__(self,kapacita):
        """ vytvoří přízdnou frontu zadané kapacity"""
        self.pole = [None]*kapacita
        self.kapacita = kapacita    #není to nutné, jde to pomocí len(self.pole)
        self.zacatek, self.pocet = 0,0

    def enqueue(self,x):
        """vloží prvek x na konec fronty, je-li volné místo"""
        if self.pocet == self.kapacita:
            raise IndexError("přeplněná fronta")
        self.pole[(self.zacatek+self.pocet)%self.kapacita] = x
        self.pocet += 1
    
    def dequeue(self):
        """odstraní a vrátí prvek ze začátku fronty je-li fronta neprázdná"""
        if self.pocet == 0:
            raise IndexError("prázdná fronta")
        self.pocet -= 1
        x = self.pole[self.zacatek]
        self.zacatek = (self.zacatek + 1)%self.kapacita
        return x

class Uzel:
    """Lineární spojové seznamy"""
    def __init__(self, x=None,dalsi=None):
        self.info = x
        self.dalsi = dalsi

class ZasobnikSpojovySeznam:
    def __init__(self):
        """vytvoří prázdný seznam"""
        self.hlava = None #hlava seznamu
    def push(self,x):
        """vloží x do hlavy spojového seznamu"""
        self.hlava = Uzel(x,self.hlava)
    def pop(self):
        """odebere a vrátí první prvek seznamu"""
        #předpokládá neprázdný zásobník
        x = self.hlava.info = self

class FrontaSpojovySEznam:
    def __init__(self):
        self.konec = None #vytvoř prázdný seznam
        self.delka = 0
    def dequeue(self):
        #předpokládá neprázdnou frontu
        x = self.konec.dalsi # hlava k odebrání
        if self.delka == 1:
            self.konec = None #fronta se vyprázdnila
        else:
            self.konec.dalsi = x.dalsi #přeskoč původní
        self.delka -= 1
        return x.info
    def enqueue(self,x):
        """vloží x na konec fronty"""
        novy = Uzel(x) #vytvoř nový uzel
        if self.dela == 0: #vytvoř cyklickou frontu
            novy.dalsi = novy
        else:
            novy.dalsi = self.konec.dalsi #nový odkazuje na začátek, to je místo kam odkazoval starý konec
            self.konec.dalsi = novy #starý konec odkazuje na nový konec
        self.konec = novy
        self.delka += 1

def palindrom(s):
    if len(s) <= 1:
        print("Báze rekurze pro řetězec",s, ", vracím True")
        return True
    else:
        print("Provnam", s[0],"vs.",s[-1])
        print("Uzavírám rekurzivní krok pro řetězec",s,", vracím True")
        return s[0] == s[-1] and palindrom(s[1:-1])

def palindrom_iter(s):
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            return False
    return True

#palindrom("madam")

def hanoj(n,odkud,kam,rezervni):
    if n== 1:
        print("přesuň koutoř z věžě", odkud, "na věž", kam)

class VrcholBinStromu:
    """třída pro reprezentaci vrcholu binárního stromu"""
    def __init__(self,x=None,levy=None,pravy=None):
        self.info = x #data
        self.levy = levy #levé dítě
        self.pravy = pravy #pravé dítě
        #spojový seznam