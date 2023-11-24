seznam = []
x = int(input())
seznam.append(x)
x = int(input())

while x != -1:
    if x >= seznam[len(seznam)-1]:
        seznam.append(x)
    x = int(input())

for i in seznam:
    print(i)