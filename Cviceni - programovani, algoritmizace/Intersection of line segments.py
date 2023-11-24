def najdi_vektory():

    def najdi_body():

        vstup = input()
        vstup = vstup.split()
        A = []
        B = []
        C = []
        D = []
        body = {"A":A,"B":B,"C":C,"D":D}
        for b in body:
            for j in range(2):
                body[b].append(int(vstup.pop(0)))
        return body

    body = najdi_body()

    AB = [body["B"][0] - body["A"][0], body["B"][1] - body["A"][1]]
    CD = [body["D"][0] - body["C"][0], body["D"][1] - body["C"][1]]

    def vyres_dve_rovnice_o_dvou_neznamych(a,b,c,d,e,f,g,h):
        """rovnice ve tvaru:
            a + bt = c + ds
            e + ft = g + hs"""
        if b == 0:
            if d == 0:
                if c-a != 0:
                    #není řešení
                    print("NE")
                else: #0t = 0s + 0 - nekonečně mnoho řešení
                    if f == 0: 
                        if h == 0:
                            if (g-e != 0):
                                print("NE")
                            else:
                                print("ANO")
                        else:
                            s = (e-g)/h
                            if s >= 0 and s <= 1:
                                print("ANO")
                            else:
                                print("NE")
                    else:   
                        if h == 0:
                            t = (g-e)/f
                            if t >= 0 and t <= 1:
                                print("ANO")
                            else:
                                print("NE")
                        else:
                            print("ANO")
            else:
                #z první rovnice
                s1cit = (a-c)
                s1jmen = d 
                s1 = s1cit/s1jmen
                if s1 <0 or s1 > 1:
                    print("NE")
                elif f == 0:
                    if h == 0:
                        if g-e == 0:
                            print("ANO")
                        else:
                            print("NE")
                    else:
                        s2cit = (e-g)
                        s2jmen = h
                        if s1 != s2cit/s2jmen:
                            print("NE")
                        else:
                            print("ANO")
                else:
                    t = (h*s1 + g - e)/f
                    if t >= 0 and t <= 1:
                        print("ANO")
                    else:
                        print("NE")

        else:
            if (f*d-b*h) == 0:
                if (f*c-f*a) == (b*g-b*e):    
                    mint = (d*0 + c - a)/b
                    maxt = (d*1 + c - a)/b
                    if (mint >= 0 and mint <= 1) or (maxt >= 0 and maxt <= 1) or (0 >= mint and 0 <= maxt) or (1 >= mint and 1 <= maxt): 
                    #zkontrolovat zda ty intervaly mají společný bod
                        print("ANO") 
                    else:
                        print("NE")
                else:
                    print("NE")
            else:
                s = (b*g-b*e-f*c+f*a)/(f*d-b*h)
                if s < 0 or s > 1:
                    print("NE")
                else:
                    t = (d*s+c-a)/b
                    if t >= 0 and t <= 1:
                        print("ANO")
                    else:
                        print("NE")

    vyres_dve_rovnice_o_dvou_neznamych(body["A"][0],AB[0],body["C"][0],CD[0],body["A"][1],AB[1],body["C"][1],CD[1])

najdi_vektory()

