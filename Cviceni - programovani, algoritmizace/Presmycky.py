def presmycky(slovo, presmycka): #slovo jsou písmena, která nám stále zbývají, přesmyčka je to, co aktuálně tvoříme
    if slovo == []:
        print(*presmycka, sep="")
    else:
        for pismeno in slovo:
            presmycka.append(pismeno)            
            presmycky(), presmycka)

print(presmycky(["k","o","z","a"],[]))