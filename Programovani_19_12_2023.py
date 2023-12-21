A = [2,4,1,76,45,18,29,32,54,22,11,28]

JA = "ja"
SOUPER = "souper"

def OKolikMuzuVyhrat( kdoHraje, zac, kon, kolikJa, kolikSouper ):
    print(f"{"   "*(len(A)-zac+kon)} {kdoHraje} {zac} {kon} {kolikJa} {kolikSouper} ")
    if zac > kon:
        return kolikJa-kolikSouper
    if kdoHraje == JA:
        a = OKolikMuzuVyhrat(SOUPER,zac+1,kon,kolikJa+A[zac],kolikSouper)
        b = OKolikMuzuVyhrat(SOUPER,zac,kon+1,kolikJa+A[kon],kolikSouper)
        return max(a,b)
    else:
        a = OKolikMuzuVyhrat(JA,zac+1,kon,kolikJa,kolikSouper+A[zac])
        b = OKolikMuzuVyhrat(JA,zac,kon+1,kolikJa,kolikSouper+A[kon])
        return min(a,b)

print(OKolikMuzuVyhrat("ja",0,len(A)-1,0,0))


import numpy as np

a = np.arange(20)
print(a)
b = a.reshape(4,5)
print(b)
a[0] = 777
print(a)
print(b)

m = a < 6
print(m)#vypíše True/False

neinicializovane = np.empty( (10,10) )
print(neinicializovane)

nuly = np.zeros( (3,4) )
print(nuly)

a = np.array([1,2,3,4,5,6,7])
print(a)
a[0] = 2.7 
print(a[0]) #vytiskne 2, vytvořilo to pole celých čísel, takže sem patří jen celá čísla
print(a.dtype) #mají omezený rozsah


import time
import matplotlib.pyplot as plt
import math

def Doba_List_Append(L,kolik):
    start = time.time()
    for _ in range(kolik):
        L.append(1)
    return time.time()-start

def Doba_List_Pop(L,kolik):
    start = time.time()
    for _ in range(kolik):
        L.pop()
    return time.time()-start

def Doba_List_Pop0(L,kolik):
    start = time.time()
    for _ in range(kolik):
        L.pop(0)
    return time.time()-start

"""
L = []
kolik = 1_000
for i in range(200):
    plt.plot([i+0.5],[Doba_List_Append(L,i*kolik)],"ro")
    L0 = list(L)
    plt.plot([i],[Doba_List_Pop(L,i*kolik)],"bo")
    plt.plot([i],[Doba_List_Pop0(L0,i*kolik)],"go")
    plt.pause(0.1)
    plt.show(block=False)
plt.show()
"""

"""
for i in range(100):
    plt.plot([i], [math.sin(i/10)],'ro' )
    plt.pause(0.1)
    plt.show(block=False)
#plt.show()
"""

plt.subplot(211) #řádky, sloupce, číslo - kolikátý teď bude graf
plt.plot([1,2,3])
plt.subplot(212)
plt.plot([4, 5, 6])
#plt.show()

plt.bar(["a","b","c","d"],[1,2,3,4])
#plt.show()

plt.plot( [0.01,0.02,0.03,0.07,0.08], [2,1,4,3,5], "ro" )
#ro - červené kolečko - red o = kolečko
plt.xlabel('osa x')
plt.ylabel('hodnoty')
#plt.show()


x = list( range(360) )
y = [math.sin(x/360*2*math.pi) for x in
range(360)]
plt.plot( x,y, "gx" ) #gx - zelené křížky
#plt.show()

plt.plot( [2,1,4,3,5] ) #nezadali jsme mu x, domyslel si je - 0-4

plt.plot( [2,1,4,3,5], [1,2,3,7,8] )

plt.plot( [0.01,0.02,0.03,0.07,0.08], [2,1,4,3,5], color=(1,1,0) )

#plt.show()
