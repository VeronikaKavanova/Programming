def PridejNulyZleva(delka, cislo):
    return (delka-len(str(cislo)))*"0"+str(cislo)
    
def PrectiAVratJednoCisloZeVstupu(zbytek):
    # zbytel obsahuje cisla zbyla od minule
    while zbytek == []:
        zbytek.extend(input().split()) #přidá seznam 
    prvni = zbytek[0]
    zbytek.remove(prvni)
    return int(prvni)


#zbytek = []
def PrectiAVratJednoCisloZeVstupu_2():
    global zbytek
    # zbytel obsahuje cisla zbyla od minule
    while zbytek == []:
        zbytek = input().split()
    prvni = zbytek[0]
    zbytek.remove(prvni)
    return int(prvni)

def PrectiAVratJednoCisloZeVstupu_1():
    return int(input())

# invariant v proměnné max je nejvetsi hodnota ze vsech, ktere jsem zatim precetl - potrebuju, aby to porad platilo
zbytek = []
maxi = PrectiAVratJednoCisloZeVstupu(zbytek)
x = PrectiAVratJednoCisloZeVstupu(zbytek)
while x != -1:
    if x > maxi:
        maxi = x
    x = PrectiAVratJednoCisloZeVstupu(zbytek)

print(maxi)

print("---------------------------------------")

def A():
    x = 5
    def B():
        nonlocal x #není globální, ale není lokální té funkce
        print(x)
        x = 88 

    B()
    print(x)

A()

def A():
    x = 5
    def B():
        print(x)
        #x = 88 ale dosazovat nemůžu, když chci dosazovat, myslí si, že je lokální

    B()
    print(x)


A() #vytisknou se dvě pětky, čte proměnnou, která není lokální, to je v pořádku


def VytiskniTabulkuMaleNasobilky(): #máme jen jednu funkci, ostatní jsou vnitřní, nikoho nezajímají
    def RadkaX():
        """funkce, která vytiskne řádku X""" 
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    def Nadpis():
        print("X    X    1    2    3    4    5    6    7    8    9   10  X")

    def Nasobky(k):
        print(f"X {k:2} X", end = " ")
        for i in range(1,11):
            print(f" {k*i:3}",end = " ")
        print(" X ")

    RadkaX()
    Nadpis()
    RadkaX()
    for i in range(1,10+1):
        Nasobky(i)
    RadkaX()

#print = 29 teď je to integer, už nemůžeme používat funkci print()

def DosadDoX():
    global X
    print(f"ve funkci X={X}")
    X = 57

X = 5
DosadDoX()
print(X)

def DosadDoX():
    X = 57

DosadDoX()

#print(X) - nebude fungovat, X neexistuje, byla to lokální proměnná

X = 5
print(X)

def PridejPrvky789(kam):
    kam = [7,8,9] #kam má adresu prázdného seznamu. Ale pak to přepíše, dosadí tam adresu nového seznamu. Pak přestane existovat

x = []
PridejPrvky789(x)
print(x)

def PridejPrvek7 (kam):
    kam.append(7)       #tady má adresu toho prvku, toho prázdného seznamu, pracuje s jeho funkcemi

x = []
PridejPrvek7(x)
print(x)

def Dosad7(kam):
    kam = 7

x = 5
Dosad7(x) 
print(x) 

def f(a,b,c):
    print(a,b,c)

f(b=30,a=7,c=89)

def RadkaX():
    """funkce, která vytiskne řádku X""" #dokumentace, když se sem vrátím, tak vím, když píšu tu funkci, tak mi to napovídá
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

def Nadpis():
    print("X    X    1    2    3    4    5    6    7    8    9   10  X")

def Nasobky(k):
    print(f"X {k:2} X", end = " ") #{k:2} - na kolik míst to chci vytisknout
    for i in range(1,11):
        print(f" {k*i:3}",end = " ")
    print(" X ")

def VytiskniTabulkuMaleNasobilky():
    RadkaX()
    Nadpis()
    RadkaX()
    for i in range(1,10+1):
        Nasobky(i)
    RadkaX()

