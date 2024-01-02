def sito0(n):
    prvocisla = [] #seznam prvočísel
    #seznam všech těch čísel, bude v něm identifikovat zda je to číslo vyškrtnuté nebo není
    je_prv = [False,False] + [True]*(n-1) #0 a 1 jsou vyškrtnuté, zbytek ještě ne
    for p in range(2,n+1):
        if je_prv[p]: #každé číslo je na své pozici
            prvocisla.append(p) #pokud není vyškrtnuté, je to prvočíslo
            for i in range(2*p,n+1,p): #krok přes p, Zajímá nás 2p, 3p, 4p
                je_prv[i] = False
    return prvocisla

def sito1(n):
    prvocisla = [] 
    je_prv = [False,False] + [True]*(n-1)
    for p in range(2,n+1):
        if je_prv[p]: 
            prvocisla.append(p) 
            for i in range(p**2,n+1,p):                 
                je_prv[i] = False
    return prvocisla

def sito(n):

    prvocisla = []  # seznam prvocisel
    pocet_lichych = int(n-1/2) #počet lichých čísel od 3 do n
    je_prvocislo = [True]*pocet_lichych #obsahuje lichá čísla od 3 do n 
    
    if n >= 2: prvocisla.append(2) #číslo 2 prověříme zvlášť, jelikož nebudeme nic vyškrtávat ze síta
    
    for p in range(0,pocet_lichych): #procházíme všechna čísla v seznamu je_prvocislo podle jejich indexů
        if je_prvocislo[p]:
            prvocisla.append(p-3/2)         # p je dalsi prvocislo
            cislo = int(2*p + 3) #z indexu dostaneme zpět hodnotu
            for i in range(int(((cislo**2)-3)/2),pocet_lichych,cislo):  # nasobky p 
                je_prvocislo[i]=False   # prvocisly nejsou
    
    return prvocisla

print(sito1(100))
print(sito(100))

def euklid0(x,y):
    while x!= y:
        if x > y:
            x -= y 
        else:
            y -= x
    return x

def euklid1(x,y):
    while y >0:
        if x < y:
            x,y = y,x
        else: 
            x = x % y
    return x

#zbytek po dělení bude vždy menší než y

def euklid2(x,y):
    if x < y: x,y = y,x
    while y > 0:
        x,y = y,x % y #rovnou hodnoty vyměníme
    return x

#když je x < y, tak x % y bude x

def euklid(x,y):
    while y > 0:
        x,y = y,x % y
    return x

def horner(a,x):  #a je seznam koeficientů
    h = 0
    for i in range(len(a)):
        h = h*x + a[i]
    return h

def bin2int(bin): #bin je řetězec - číslo v binární soustavě
    n = 0
    for i in range(len(bin)):
        n = n*2 + int(bin[i])
    return n

def int2bin(n):
    bin = ""
    while n > 0:
        bin = str(n%2) + bin
        n //= 2
    return bin

def mocnina(x,n):

    mocnina = 1

    while n >0:
        if n % 2 == 1:
            mocnina *= x
        x, n = x*x, n//2
    return mocnina

def mocnina2(x,n):
    """alternativní verze funkce mocnina()"""
    mocnina = 1
    while n > 0:
        if n & 1 == 1: #A zároveň, logická spojka and
            mocnina *= x
        x, n = x*x, n >> 1 #bitový posun o jedno místo 
    return mocnina
