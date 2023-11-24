#chceme určit nejčastější slovo ze vsech, ktera jsme dostali
# na vstupu je posloupnost ukoncena "", ktera uz se nepocita
slova = []
pocty = []

x = input()
while x != "":
    if x in slova:
        pocty[slova.index(x)] += 1
    else:
        slova.append(x)
        pocty.append(1)
    x = input()

maxpocet = max(pocty)
maxslovo = slova[pocty.index(maxpocet)]
print( f"1: Nejcastejsi slovo: {maxslovo} a bylo tam {maxpocet}-krat") 


input = ("--------")

# příklad 1 - chceme určit nejcastejsi cislo ze csech, která jsme dostali
# tzn. že chceme přečíst všechna čísla
# jak vědět že je konec
# na vstupu je posloupnost ukoncena - 1, ktera uz se nepocita
#potrebujeme určit to nejcastejsi => musime si pamatovat počty všech čísel
# dvě pole - stejně dlouhá - v prvním čísla, v druhém počty

cisla = [] #cisla, která jsme dosud videli
pocty = [] #a jejich pocty

x = int(input())
while x!= -1:
    #zpracovat tohle cislo    
    if x in cisla:
        pocty[cisla.index(x)] += 1
    else:
        cisla.append(x)
        pocty.append(1)
    x = int(input())

# pak musíme vybrat nejčastější
# najdeme největší číslo v poctech - máme funkci max()
maxpocet = max(pocty)
maxcislo = cisla[pocty.index(maxpocet)]
print( f"1: Nejcastejsi cislo: {maxcislo} a bylo tam {maxpocet}-krat") # takhle se používají stringy s f

for i in range(len(cisla)):
    if pocty[i] == maxpocet:
        print( f"2: Nejcastejsi cislo: {cisla[i]} a bylo tam {maxpocet}-krat")
        


i = input("-----------")

s = input("Zadejte řadu čísel, která mám sečíst")
ss = s.split()
soucet = 0
for i in ss:
    soucet += int(i)
print(soucet)


i = input("--------------")

N = 1

while True:
    delitel = 2
    jeToPrvocislo = True

    while delitel**2 < N:
        if N % delitel == 0:
            jeToPrvocislo = False
            break
        delitel += 1

    if jeToPrvocislo == True:
        print(N)
    N += 2