k = int(input())

sloupcu = 1 + 2*(k-1)

def tiskni_ker(k,sloupcu):
    hvezd = 1
    for i in range(1,k+1):
        tecek = (sloupcu-hvezd)//2
        print("."*tecek + "*"*hvezd + "."*tecek)
        hvezd += 2

tiskni_ker(k,sloupcu)