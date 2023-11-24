velikost = int(input())
pocet = int(input())

def nakresli_sachovnici(velikost,pocet):

    radku = pocet*velikost

    for radek in range(1,radku+1):
        seznam = []
        if radek%(velikost*2) <= velikost and radek%(velikost*2) > 0:
            pozice = 1
        else:
            pozice = -1
        for i in range(1,radku+1): #sloupcu je stejne jako radku
            if pozice == 1:
                znak = "."
            else:
                znak = "*"            
            if i%velikost == 0:
                pozice *= -1
            seznam.append(znak)
        print(*seznam, sep = "")

"""
    def nakresli_policko(velikost, pozice):
        if pozice == 1:
            znak = "."
        else:
            znak = "*"
        for i in range(velikost):
            print(velikost*znak)
    
    pozice = 1

    for i in range(pocet):
        for j in range(pocet):
            nakresli_policko(velikost,pozice)
            pozice *= -1 
"""

nakresli_sachovnici(velikost,pocet)