import matplotlib.pyplot as plt
import numpy as np
import math

def get_number(msg):
    while True:
        try:
            number = int(input(msg))
            if number >= 0:
                return number
            else:
                print("To číslo nebylo přirozené.")
        except:
            print("To nebylo celé číslo.")


options = [1, 2, 3, 4, 5]

while True:
    uloha = get_number("Zadejte číslo 1-5 pro volbu úlohy, kterou má program vykonávat:\n\t 1. Papoušek, program vypíše, co zadáte.\n\t 2. Vykresli sinusovku na definičním oboru (-2;2).\n\t 3. Sečte všechna přirozená čísla od jednoho zadaného po druhé. \n\t 4. Vypíše mi vaše jméno, příjmení, třídu, skupinu Fj nebo Nj a skupinu Aj.\n\t 5. Program se ukončí. \n")
    if uloha not in options:
        print("Tohle nebyla možnost.")
        continue
    
    if uloha == 1:
        papousek = input("Napište, co chcete, aby papoušek zopakoval: ")
        print(papousek)
    elif uloha == 2:
        plt.xlim(-2.2, 2.2)
        plt.ylim(-1.3, 1.3)
        x = np.linspace(-2, 2, 1000)
        y = np.sin(x)
        plt.plot(x, y)
        plt.show()
    elif uloha == 3:
        mini = get_number("Zadej nejmenší číslo: ")
        while True:
            maxi = get_number("Teď zadej největší číslo: ")
            if maxi > mini:
                break
            else:
                print("Tohle číslo musí být větší než to první.")
        soucet = mini
        pricitame = (mini + 1)
        for i in range(maxi - mini):
            soucet += pricitame
            pricitame += 1
        print(soucet)
    elif uloha == 4:
        print("Jmenuji se Veronika Kavanová, chodím do 7.S, jsem ve skupině Aj1 a chodím na francouzštinu.")
    else:
        print("Tak se měj.")
        break
            
                
