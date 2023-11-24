class kontrola:
    
    def __init__(self):
        self.zavorky = {"(":")","[":"]","{":"}","<":">"}
    
    def najdi_konec(self,zavorka, vstup):
        while vstup != []:
            znak = vstup.pop()
            if znak == self.zavorky[zavorka]:
                return vstup
            elif znak in self.zavorky:
                vysledek = self.najdi_konec(znak,vstup)
                if vysledek == False:
                    return False
            else:
                return False
        return False

def zkontroluj_vse(zasobnik, kontrola):

    while zasobnik != []:
        zavorka = zasobnik.pop()
        if zavorka in kontrola.zavorky:
            vysledek = kontrola.najdi_konec(zavorka,zasobnik)
            if vysledek == False:
                return False
            else:
                zasobnik = vysledek
        else:
            return False
    return True

vstup = input()

zasobnik = []

for i in vstup[-1::-1]:
    zasobnik.append(i)

kontrola = kontrola()

print(zkontroluj_vse(zasobnik,kontrola))
