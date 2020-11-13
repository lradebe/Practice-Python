from math import *

def simple_interest(P, r, t):

    """This function calculates user input simple interest"""

    A = (P * (1 + ((r / 100) * t)))
#A is the Simple interest (final amount)

    print("\nThe final amount through simple interest is:",str(A))

#P : Principal amount
#r : interest rate
#t : time/period

simple_interest(P,r,t)


