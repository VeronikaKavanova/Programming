import math

#iterace = int(input())

def spocti_delku1(iterace):
    if iterace == 0:
        return 1
    else:
        return (4/3)*spocti_delku1(iterace-1)

def spocti_delku2(iterace):
    return ((4/3)**iterace)

def obsah(n, l):
    if n == 0:
        return 0
    else:
        area = (((l/3)**2 * math.sqrt(3)) / 4) + 4 * obsah(n-1, l/3)
        return area

for i in range(100):
    print(obsah(i, 1))
#print(spocti_delku1(iterace))
#print(spocti_delku2(iterace))
    
    