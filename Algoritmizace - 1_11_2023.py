#vyhledávání v poli
#vstup: pole a indexované od 0, prvek x
#výstup: pokud se x v a vyskytuje, index výskytu, jinak false

#nejjednoduší metoda - sekvenční průchod
#projdeme všechny prvky

def hledej (a,x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return False

#složitost v nejhorším případě je n - délka seznamu

print(hledej([10,20,30],10))

#vyhledávání v poli se zarážkou
def hledej1(a,x):
    a.append(x) #hledaný prvek je zarážka, vložíme ho na konec seznamu
    n = len(a)-1 #index zarážky
    i = 0
    while a[i] != x: #x je vždy nalezeno
        i += 1
    del a[n]
    if i ==n:
        return False
    else:
        return i

#vyhledávání v uspořádaném poli
#binární vyhledávání

def binSearch(a,x):
    dolni, horni = 0, len(a) - 1
    #invariant: pokud je x v seznamu, tak leží v uzavřeném intervalu [dolni,horni]
    while dolni <= horni:
        stred = (dolni+horni)//2
    if a[stred] == x:
        return stred
    elif a[stred] < x:
        dolni = stred + 1
    else:
        horni = stred - 1
    return False

#pokud je tam více výskytů, tak najde některý z nich

a = [10,20,45,78,23,2,0,65,1,11,32]
print(binSearch(a,32))

#chtěli bychom zobecnit funkci binSearch(a,x) tak, aby v setříděném poli a nalezla všechny výskyty prvku x - dú

def odmocnina(n): #za předpokladu, že n > 1
    """Výpočet odmocniny z n půlením intervalu"""
    eps = 0.01
    dolni,horni = 1.0, n
    stred = (dolni+horni)/2.0
    mocnina = stred**2
    while abs(mocnina - n) >= eps: #kontrolujeme zda se naše řešení příliš neliší - kvůli zaokrouhlovací chybě
        if mocnina < n:
            dolni = stred
        else:
            horni = stred
        stred = (dolni + horni)/2.0
        mocnina = stred**2
    return stred

def bubbleSort(a):
    n = len(a)
    for i in range(n-1,0,-1): #n-1 >= i >= 1
        #invariant: prvky a[i+1:n] jsou na svých místech
        for j in range(i): #0 <= j <= i -1
            #invariant: prvek a[j] = max a[0...j]
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            #a[i] = max a[0...i]
            #invariant vnitřního cyklu nám umožňuje to, že platí invariant vnějšího cyklu

def selectionSort(a):
    n = len(a)
    for i in range(n-1):
        #a[i] vyměn s minimem z a[i:]
        minIndex, minHodnota = i, a[i]
        #dočasné minimum
        for j in range(i+1,n):
            if minHodnota > a[j]:
                minHodnota = a[j]
                minIndex = j
        a[i], a[minIndex] = a[minIndex], a[i]

        print(a, "delka setrideneho useku", i+1)

a = [45, 23, 4564, 8789, 789 , 45, 32, 55,21, 3212,3, 2123,21, 32,132]
print(selectionSort(a))

def insertionSort(a):
    n = len(a)
    for i in range(1,n):
        #vlož a[i] do setříděného a[:i]
        x, j = a[i], i -1
        while j >= 0 and a[j] > x:
            a[j+1] = a[j]
            j -= 1
        a[j + 1] = x

    print(a,"delka setrideneho useku", i+1)

a = [45, 23, 4564, 8789, 789 , 45, 32, 55,21, 3212,3, 2123,21, 32,132]
insertionSort(a)
#invariant cyklu: na začátku každé iterace je prvních i prvků již setříděno
