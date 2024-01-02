#vygenerovat všechny čísla složená z číslic na vstupu, která jsou dělitelná třemi
soubor = input().split()
for i in range(len(soubor)):
    soubor[i] = int(soubor[i])

def cisla_delitelne_tremi(soubor):

    def vsechny_kombinace(aktualni, soubor):
        kombinace.append(aktualni)
        for i in soubor:
            vsechny_kombinace(aktualni + [i], soubor[soubor.index(i)+1:])
    
    def delitelne_tremi(kombinace):
        kombinace_delitelne_tremi = []
        for jedna_kombinace in kombinace:
            soucet = 0
            for i in jedna_kombinace:
                soucet += i
            if soucet % 3 == 0:
                kombinace_delitelne_tremi.append(jedna_kombinace)
        return kombinace_delitelne_tremi

    def vsechny_permutace(aktualni, zbyva, uloziste):
        if zbyva == []:
            return uloziste.append(list(aktualni))
        for i in zbyva:
            aktualni.append(i)
            index = zbyva.index(i)
            vsechny_permutace(aktualni, zbyva[:index] + zbyva[index+1:], uloziste)
            aktualni.pop()

    kombinace = []

    vsechny_kombinace([],soubor)
    kombinace_delitelne_tremi = delitelne_tremi(kombinace)
    #print(kombinace_delitelne_tremi)
    permutace = []
    for cislo in kombinace_delitelne_tremi:
        if cislo != []:
            vsechny_permutace([],cislo, permutace)
    permutace_bez_duplikatu = set()
    for objekt in permutace:
        cislo = 0
        rad = 1
        for i in objekt:
            cislo = rad*i + cislo
            rad *= 10
        permutace_bez_duplikatu.add(cislo)
    print(*permutace_bez_duplikatu, sep= "\n")

cisla_delitelne_tremi(soubor)
    