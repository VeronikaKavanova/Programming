def je_na_radku_kapka(radek):
    kapky = ["\\","/","X"]
    for znak in radek:
        if znak in kapky:
            return True
    return False

def steceni_kapeck(radek):
    
    def kapka_doleva():
        novy_index = index - 1
        if novy_index >= 0:
            if novy_radek[novy_index] == "-":
                novy_radek[novy_index] = "/"
            else:
                novy_radek[novy_index] = "X"
    
    def kapka_doprava():
        novy_index = index + 1
        if novy_index < len(novy_radek):
            if novy_radek[novy_index] == "-":
                novy_radek[novy_index] = "\\"
            else:
                novy_radek[novy_index] = "X"
    
    stary_radek = radek
    novy_radek = ["-"]*len(stary_radek)
    for index in range(len(stary_radek)):
        znak = stary_radek[index]
        if znak == "/":
            kapka_doleva()        
        elif znak == "\\":
            kapka_doprava()
        elif znak == "X":
            kapka_doleva()
            kapka_doprava()
    
    return novy_radek

radek = input()

while je_na_radku_kapka(radek) != False:
    print(*radek, sep="")
    radek = steceni_kapeck(radek)