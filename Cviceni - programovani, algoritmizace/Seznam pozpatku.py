seznam = []
x = int(input())

while x != -1:
    seznam.insert(0,x)
    x = int(input())

for i in seznam:
    print(i, end = " ")