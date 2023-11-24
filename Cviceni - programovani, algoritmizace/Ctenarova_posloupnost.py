prvni_cislo = str(int(input()))
kolik_cisel = int(input())

def precti_cislo(cislo):
    nove_cislo = ""
    kolik = 1
    for i in range(len(cislo)):    
        cislice = cislo[i]
        if i+1 < len(cislo): 
            if cislo[i] == cislo[i+1]:
                kolik += 1
            else:
                nove_cislo += str(kolik) + cislice
                kolik = 1
        else:
            nove_cislo += str(kolik) + cislice
    print(nove_cislo)
    return nove_cislo

cislo = prvni_cislo
for i in range(kolik_cisel):
    cislo = precti_cislo(cislo)


