#vygenerovat všechny čísla složená z číslic na vstupu, která jsou dělitelná třemi
#soubor = input().split()
soubor = [1,5,3,9,4,2]

#integer *10 + nova_hodnota

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

    def vsechny_permutace(aktualni, zbyva):
        if zbyva == []:
            return print(aktualni)
        for i in zbyva:
            aktualni.append(i)
            index = zbyva.index(i)
            vsechny_permutace(aktualni, zbyva[:index] + zbyva[index+1:])
            aktualni.pop()

    kombinace = []

    vsechny_kombinace([],soubor)
    kombinace_delitelne_tremi = delitelne_tremi(kombinace)
    print(kombinace_delitelne_tremi)
    #vsechny_permutace([],kombinace_delitelne_tremi)

cisla_delitelne_tremi(soubor)
    