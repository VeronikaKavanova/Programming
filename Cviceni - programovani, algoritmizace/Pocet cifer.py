import math

number = int(input())
test = 10
digits = 0
while digits == 0:
    if number < test:
        digits = int(math.log10(test))
        print(digits)
    else:
        test *= 10

