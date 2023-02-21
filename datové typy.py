ntice = (1,2,4,3)
seznam = list(ntice)

import numpy as np

matice = np.zeros((10,10), dtype = float)

matice[5,5] = 325.7

print(matice[5,5])
print(matice)

#množiny -> set
mnozina = {1,2,3,4,5}
m2 = {2,3,4}
m3 = {4,5,6}

print(mnozina <= m2)
print(m3 <= mnozina)
print(m2 <= mnozina)

dvekostky = {x+y for x in range(1,7) for y in range(1,7)}
print(dvekostky)

ukazkovyslovnik = {}
slovnik = {"borec":"Pepa", "šmatlák":"Karel", "heslo":"křeslo"}

for klic in slovnik.keys():
    print(f"{klic} {slovnik[klic]}")

print(slovnik["borec"])


figurky = {"černý pěšák 1":{"x":"1", "y":"2", "jméno":"brzo umře 1"}}

print("Jaké má hodnoty figurka?", figurky["černý pěšák 1"].keys())
print(figurky.keys())
figurky["Queen"]={"x":"1", "y":"2", "jméno":"Victoria"}

if(figurky["Queen"]["x"] == figurky["černý pěšák 1"]["x"]):
    if (figurky["Queen"]["y"] == figurky["černý pěšák 1"]["y"]):
        print(figurky["černý pěšák 1"]["jméno"], "umřel")
