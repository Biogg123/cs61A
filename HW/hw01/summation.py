from operator import mul
#from math import pi
def cube(k):
    return pow(k, 3)

def summation(n, term):
    """ Sum the first n terms of a sequence.
    >>> summation(5, cube)
    225
    """
    total, k=0,1
    while k<=n:
          total, k= total + term(k), k+1
    return total   

 
"""a= summation(5, cube)
print(a)
"""

def pi_term(k):
    return 8/mul(4*k-3, 4*k-1)

b=summation(1000000, pi_term)
#print(b)
summation(1000000, pi_term)