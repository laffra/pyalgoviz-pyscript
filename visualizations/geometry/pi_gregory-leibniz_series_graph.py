"""
 Geometry - Pi Gregory-Leibniz Series (Graph) 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Geometry - Pi Gregory-Leibniz Series (Graph)"
__author = "laffra"

def __algorithm():
    from decimal import Decimal

    estimates = []

    # Calculate Pi using Gregory-Leibniz Series:
    #
    #  pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ....
    #
    def calculatePi(steps=100): 
        pi = 1
        for k in range(3, 2 * steps, 4):
            pi -= Decimal(1)/k
            pi += Decimal(1)/(k+2)
            estimates.append(pi * 4)
        return pi * 4

    mypi = calculatePi(300)

    print('''
    PI = %s

       pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ....

    In Carl Sagan's novel "Contact", when listing Pi in base 11,
    a circle could be seen inside Pi. This fact never made it to
    the movie.
    ''' % mypi)

def __visualization():
    import math
    
    rect(50, 30, 500, 200)
    text(15, 65, "Pi", 32)
    line(45, 50, 550, 50, "grey")
    text(290, 245, "steps", 14)

    if __lineno__ > 17:
        for n in range(len(estimates)):
            pi = estimates[n]
            error = pi - Decimal(math.pi)
            y = int(50 + error * 500)
            circle(50 + 3*n, y, 2, "red")