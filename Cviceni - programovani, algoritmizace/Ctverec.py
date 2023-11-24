n = int(input())
sloupcu = 1 + 2*(n-1)

for i in range(n):
    hvezd = i*2 + 1
    tecek = (sloupcu-hvezd)//2
    print("."*tecek + "*"*hvezd + "."*tecek)

for i in range(1,n):
    hvezd = 1 + (n-1-i)*2    
    tecek = (sloupcu-hvezd)//2
    print("."*tecek + "*"*hvezd + "."*tecek)
