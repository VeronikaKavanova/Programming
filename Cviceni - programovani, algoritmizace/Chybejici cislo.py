seznam = []
x = int(input())

while x != -1:
    seznam.append(x)
    x = int(input())

seznam.sort()

def najdi_chybejici(seznam):
    minula = seznam[0]
    if minula != 1:
        return 1
    else:
        for i in range(1,len(seznam)):
            if seznam[i] != minula + 1:
                chybejici = (seznam[i]-1)
                return chybejici    
            minula = seznam[i]
    return minula + 1

print(najdi_chybejici(seznam))