import random

predpony = ["Kul", "Dul", "Bal", "Mař", "Mic", "Mour"]
pripony_F = ["ina", "ička", "inka", "a"]
pripony_M = ["ík", "oun", "íček", "ek"]
genders = [0, 0, 0, 1, 1, 1, 1]

jmena = []

for i in genders:
    if i == 0:
        while True:
            jmeno = random.choice(predpony) + random.choice(pripony_F)
            if jmeno not in jmena:
                jmena.append(jmeno)
                break
        what = "kočičku, která"
    else:
        while True:
            jmeno = random.choice(predpony) + random.choice(pripony_M)
            if jmeno not in jmena:
                jmena.append(jmeno)
                break
        what = "kocoura, který"
    print("Máte", what, "se jmenuje", jmeno + ".")
