def number(msg):
    while True:
        try:
            a = float(input(msg))
            return a
        except ValueError:
            print("Musíš zadat číslo.")

def strana():
    while True:
        a = number("Zadej délku strany v centimetrech: ")
        if a > 0:
            return a
        else:
            print("Číslo musí být kladné.")

def obdelnik(a, b):
    obvod = 2*a + 2*b
    obsah = a*b
    print("Obvod obdélníku je", obvod, "centimetrů čtverečních a obsah je", obsah, "centimetrů čtverečních")

def seznam_cisel():
    radaCisel = []
    while True:
        konec = input("Pokud už jsi se řadou spokojen, zmáčkni 'n', pokud chceš přidat do řady další číslo, zmáčkni cokoli jiného: ")
        if konec == "n":
            return radaCisel
        else:
            a = number("Zadej další číslo: ")
            radaCisel.append(a)
            
def palindrom(text):
    newtext = ""
    index = (len(text)-1)
    for i in text:
        char = text[index]
        newtext += char
        index -= 1
    print(newtext)

def srovnej(radaCisel):
    serazena = []
    for i in range(len(radaCisel)):
        nejmensi = radaCisel[0]
        for j in radaCisel:
            if j < nejmensi:
                nejmensi = j
        serazena.append(nejmensi)
        radaCisel.remove(nejmensi)
    print(serazena)
    
a = strana()
b = strana()
obdelnik(a, b)

text = input("Zadej nějaký text: ")
palindrom(text)

radaCisel = seznam_cisel()
srovnej(radaCisel)
