def gcd(x,y):
    while y > 0:
        x,y = y,x % y 
    return x

class Fraction:
    def __init__(self,num,den):
        divisor = gcd(num,den)
        self.num = num // divisor
        self.den = den // divisor
        #objekt "není dotvořený" dokud neskončí konstruktor, nemůžeme použít simplify()

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def simplify(self):
        GCD = gcd(self.num,self.den)
        self.num //= GCD
        self.den //= GCD

    def add(self, other):
        num = self.den*other.num + other.den*self.num
        den = self.den * other.den
        return Fraction(num,den)

    def sub(self,other):
        num = other.den*self.num - self.den*other.num 
        den = self.den * other.den
        return Fraction(num,den)

    def multiply(self,other):
        num = self.num*other.num
        den = self.den*other.den
        return Fraction(num,den)

    def divide(self,other):
        num = self.num*other.den
        den = self.den*other.num
        return Fraction(num,den)

first = Fraction(3,5)
second = Fraction(6,4)

result = first.add(second)
print(result)
