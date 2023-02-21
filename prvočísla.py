prvocisla = []
cisla = []
neprvocisla = []
for i in range(2, 1000):
    cisla.append(i)
    for j in range(2, (i-1)):
        if i%j == 0:
            neprvocisla.append(i)
            break
for i in cisla:
    if i not in neprvocisla:
        prvocisla.append(i)
print(prvocisla)



cisla = []
for i in range(2, 1000):
    cisla.append(i)
    for j in range(2, (i-1)):
        if i%j == 0:
            cisla.remove(i)
            break
print(cisla)
