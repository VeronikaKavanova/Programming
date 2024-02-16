
def generuj_druhym_zpusobem(policka, prazdna_policka, hotovo):
    """Vygeneruje náhodné sudoku s daným počtem číslic, tak, že začne od prázdné tabulky a rekurzivně je zkouší 
    doplnit"""

    print(hotovo)

    if hotovo == znat:
        unikatni = jedno_reseni(policka, prazdna_policka)
        if unikatni == True:
            return policka
        else:
            return False
    
    policka_na_zkouseni = prazdna_policka
    
    vysledek = False

    while vysledek == False:
        
        if policka_na_zkouseni == []:
            return False

        pole = random.choice(policka_na_zkouseni)
        policka_na_zkouseni = odstran_hodnotu_ze_seznamu(policka_na_zkouseni, pole)
        
        hodnoty_na_zkouseni = pole.mozne_hodnoty

        vysl = False

        while vysl == False:

            if hodnoty_na_zkouseni == []:
                break
            
            nova_hodnota = random.choice(hodnoty_na_zkouseni)
            pole.vepis_hodnotu(nova_hodnota)
            hodnoty_na_zkouseni = odstran_hodnotu_ze_seznamu(hodnoty_na_zkouseni, nova_hodnota)

            nova_prazdna_policka = odstran_hodnotu_ze_seznamu(prazdna_policka, pole)

            vysl = generuj_druhym_zpusobem(policka, nova_prazdna_policka, hotovo + 1)

            if vysl == False:
                pole.smaz_hodnotu()
            else:
                vysledek = policka

    return policka

vepsane_mozne_hodnoty = [1,2,3]
napis = " ".join(str(cislo) for cislo in vepsane_mozne_hodnoty)
print(napis)