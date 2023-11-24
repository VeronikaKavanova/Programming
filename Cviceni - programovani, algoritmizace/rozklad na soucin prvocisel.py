delitele = []
prvocisla = []

x = int(input())

delitele.append(x)

def najdi_delitele(x):
    for i in range(2,x):
        if x%i == 0:
            x = x//i
            delitele.append(i)
            delitele.append(x)
            return x            
    prvocisla.append(x)

while delitele != []:
    d = delitele[0]
    najdi_delitele(d)
    delitele.remove(d)

for p in prvocisla:
    print(p)