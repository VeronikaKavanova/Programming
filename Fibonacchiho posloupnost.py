p = [1, 1]
nn = 2
print(p[0])
print(p[1])
while nn <= 10**8:
    nn = p[(len(p)-2)] + p[(len(p)-1)]
    p.append(nn)
    if nn <= 10**8:
        print(nn)
