def zaklinadlo_n_pismen(n):
    pismena = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    def generuj(hotovo, zbyva):
        if zbyva == 0:
            if hotovo == "HUBEROKORORO":
                input()                
            print(hotovo)
        else:    
            for pismeno in pismena:
                generuj(hotovo+pismeno, zbyva-1)
    generuj("", n)

zaklinadlo_n_pismen(4)

#HUBERO KORORO
#print(26**11*7 + 26**10*20 + 26**9 + 26**8*4 + 26**7*17 + 26**6*14 + 26**5*10 + 26**4*14 + 26**3*17 + 26**2*14 + 26*17 + 15)