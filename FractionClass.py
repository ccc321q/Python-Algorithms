
def findgcd(x, y):
    '''Returns the Greatest Common Deniminator of x and y. Assumes x and y are possitive integers'''
    smaller = min(x, y)
    for i in range(smaller, 1, -1):
        if x % i == 0 and y % i == 0:
            return i
    return 1


class Fraction(object):
    '''Defines a Fraction with numerator num and a non-zero int denominator'''

    def __init__(self, num=0, denom=1):
        ''' Creates a new Fraction with numerator num and denominator denom'''
        self.numerator = num
        if denom != 0:
            self.deniminator = denom
        else:
            raise ZeroDivisionError

    def reduce(self):
        '''Reduces self's fraction'''
        gcd = findgcd(self.numerator, self.denominator)
        self.numerator /= gcd
        self.denominator /= gcd
