def kolize(radek,sloupec):
    for i in range(radek):
        #prochazime vsechny predchozi radky
        if sachovnice[i] == sloupec or \
            radek-i == abs(sachovnice[i]-sloupec):
            return True #ohrozuje damu na radku i
    return False #zadnou neohrozuje

def n_dam(n):
    def gen_n_dam(radek):
        if radek == n:
            vysledek.append(list(sachovnice))
        else:
            for sloupec in range(n):
                if not kolize(radek,sloupec):
                    sachovnice[radek] = sloupec
                    gen_n_dam(radek + 1)

    vysledek, sachovnice = [], [0]*n
    gen_n_dam(0)
    return vysledek