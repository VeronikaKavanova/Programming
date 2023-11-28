from math import factorial as fact

result = fact(10)
sjednoceni = 5*fact(9) - 10*fact(8) + 10*fact(7) - 5*fact(6) + fact(5)
result -= sjednoceni
print(result)
print(120*18089)