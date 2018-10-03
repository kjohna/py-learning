#starting from code given by http://interactivepython.org/runestone/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html
#extending for "Self Check" to include methods "*, /, and -" and to implement comparison operators "> and <"
#parts added have comments
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __sub__(self, other):
        #subtract fractions
        subnum = other.num * -1
        return self + Fraction(subnum, other.den)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __mul__(self, other):
        #multiply fractions
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __div__(self, other):
        #divide fractions
        divnum = other.den
        divden = other.num
        return self * Fraction(divnum, divden)

    def __gt__(self, other):
        #self > other
        new_num_self = self.num * other.den
        new_num_other = other.num * self.den
        return new_num_self > new_num_other

    def __lt__(self, other):
        #self < other
        new_num_self = self.num * other.den
        new_num_other = other.num * self.den
        return new_num_self < new_num_other

def main():
    x = Fraction(1,2)
    y = Fraction(2,3)
    print "x = " + str(x)
    print "y = " + str(y)
    print(x+y)
    print(x == y)
    print x * y
    print x / y
    print x - y
    print x > y
    print x < y

main()
