#python 3.5.2

'''
The greatest common divisor (gcd/GCD), or the greatest common factor (gcf), 
or highest common factor (hcf), of two or more integers (at least one of which is not zero),
is the largest positive integer that divides the numbers without a remainder.

greatest common divisor calculate:
https://www.hackmath.net/en/calculator/greatest-common-divisor

divisors calculate:
https://www.hackmath.net/en/calculator/divisors

'''


#Greatest Common Divisor (gcd) is a example of HELPER METHOD

def gcd(a,b): 
    if a > b: a,b = b,a
    while True:
        if b % a == 0: return a
        a, b = b%a, a

class Fraction(object):
    def __init__(self, a, b):
        if( gcd(a,b) > 1):
            self.d =  gcd(a,b) 
            
    def answer(self):
        return self.d

# Divisors of 12 are 1, 2, 3, 4, 6,   12
# Divisors of 8  are 1, 2,    4,    8  
# ANSWER IS : 4 
            
f = Fraction(8,12)

print ( ' GCD (8,12) = {}'.format ( f.answer() ))

print( '-'*20 )

# Divisors of 6 are 1,2,3,  6
# Divisors of 8 are 1,2,  4,  8
f = Fraction(6,8)

print ( ' GCD (6,8) = {}'.format ( f.answer() ) )
print( '-'*20 )