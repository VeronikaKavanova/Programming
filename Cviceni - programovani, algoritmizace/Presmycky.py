def presmycky(slovo, presmycka):
    if slovo == "":
        print(presmycka)
    for i in range(len(slovo)):
        pismeno = slovo[i]
        presmycka = presmycka + pismeno
        presmycka = pismeno + presmycky(slovo[0:i]+slovo[i+1:], presmycka)
        return presmycka

print(presmycky("koza",""))