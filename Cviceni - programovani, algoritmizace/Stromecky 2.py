k = int(input())
l = int(input())

sloupcu = 1 + 2*(k-1)

def tiskni_strom(k,l,sloupcu):

    def tiskni_ker():
        hvezd = 1
        for i in range(k):
            tecek = (sloupcu-hvezd)//2
            print("."*tecek + "*"*hvezd + "."*tecek)
            hvezd += 2

    def tiskni_kmen():
        for i in range(l):
            tecek = (sloupcu-1)//2
            print("."*tecek + "*" + "."*tecek)
    
    tiskni_ker()
    tiskni_kmen()

tiskni_strom(k,l,sloupcu)