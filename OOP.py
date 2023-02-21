class Animal:
    def __init__(self, latinName):
        self.latinName = latinName    
    def mate(self, animal2):
        name = self.latinName + animal2.latinName
        print(f"narodilo se nám {name}")
        return Animal(name)

class Dog(Animal):
    def isAlive():
        return 1


amalka = Animal("Canis Major")
karlik = Animal("Oppus Maximus")
potomek = amalka.mate(karlik)

chip = Dog("péťa")
chip.mate(amalka)
chip.mate(potomek)
chip.isAlive()

