from math import *
def compound_interest(P, n, t, r):

    """This function returns the final amoount of a compound
    interested principal amount"""

    bracket1 = (1 + ((r / 100) / n))
    bracket2 = (n * t)
    A = P * bracket1 ** bracket2

    print("This is the final amount after compound interest:", str(A))

#P : Principal amount
#n : Number of times interest applied per time period
#t : time
#r : interest rate

compound_interest(P , n, t, r)
