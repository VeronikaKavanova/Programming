


f = open(r"C:\Programming\Programovani_1_14_11_2023.py","r",encoding="utf-8")
for radek in f:
    print(radek)
f.close()


import turtle

def Obrazek(zelva):
    for i in range(17):
        zelva.forward(100)
        zelva.left(130)
        #zelva.left(10)
################################

#funkci mam a nechci do ni sahat, ale chci obrazek zvetsit

#zmenim objekt ktery to vyuziva.
#tohle pomoci dedicnosti
class VelkaZelva(turtle.Turtle):
    def __init__(self,zvetseni=1,tloustka=1,barva=(0,0,0),rychlost=1):
        self.zvetseni = zvetseni
        super().__init__()
        self.width(tloustka)
        self.color(barva)
        self.speed(rychlost)
    def forward(self,x):
        super().forward(x*self.zvetseni)
    def left(self,uhel):
        super().right(uhel)

class NeZelva:
    def __init__(self):
        self.zelva = turtle.Turtle()
    def forward(self,x):
        self.zelva.forward(2*x)
    def left(self,uhel):
        self.zelva.left(uhel)

#rozdil mezi -NeZelvou a velkou zelvou je ze NeZelva ma vsechny ty funkce, i ty o kterych jsme nemluvili, NeZelva ma jen tyhlety 

#t = turtle.Turtle()
#t = VelkaZelva(zvetseni=0.1,tloustka=5,barva=(0,1,1),rychlost=2)
t = NeZelva()
Obrazek(t)

