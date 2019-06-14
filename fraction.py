def gcd(dividend, divisor):
    if (dividend % divisor == 0):
        return divisor
    else:
        return gcd(divisor, dividend % divisor)

class Fraction:
    def __init__(self, top, bottom):
        if type(top) != int or type(bottom) != int:
            raise RuntimeError('Fraction accepts only integer parameters')
        common = gcd(top, bottom)
        self.num = top//common
        self.den = bottom//common 

    
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        print("__add__")
        newnum = self.num * other.den + other.num * self.den
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __iadd__(self, other):
        print("__iadd__")
        self = self + other 
        return self

    def __radd__(self, other):
        print("__radd__")
        otherfr = Fraction(other, 1)
        return self + otherfr
    
    def __repr__(self):
        return ("Numerator: " + str(self.num) + ", Denominator: " + str(self.den))

    
    def __sub__(self, other):
        newnum = self.num * other.den - other.num * self.den
        newden = self.den * other.den
        return Fraction(newnum, newden)   

    def __mul__(self, other):
        newnum = self.num * other.num 
        newden = self.den * other.den 
        return Fraction(newnum, newden)
    
    def __floordiv__(self, other):
        newnum = self.num * other.den 
        newden = self.den * other.num 
        return Fraction(newnum, newden)
    
    def __truediv__(self, other):
        divres = self//other
        return divres.num / divres.den 

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den 
        return firstnum == secondnum 
    
    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den 
        return firstnum > secondnum 

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den 
        return firstnum < secondnum 
    
    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den

f1 = Fraction(3, 10)
f2 = Fraction(3, 2)
f1 += f2
print(repr(f1))
