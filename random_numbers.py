import random

x = random.randint(0,100)
y = random.randint(0,100)
soucet = x + y
soucin = x * y
if y > x:
    vetsi_cislo = y
    mensi_cislo = x
else:
    vetsi_cislo = x
    mensi_cislo = y
rozdil = vetsi_cislo - mensi_cislo
podil = vetsi_cislo/mensi_cislo
print("Čísla byla:", x, "a", y)
print("Součet čísel je:", soucet)
print("Součin čísel je:", soucin)
print("Rozdíl čísel je:", rozdil)
print("Podíl čísel je:", podil)
