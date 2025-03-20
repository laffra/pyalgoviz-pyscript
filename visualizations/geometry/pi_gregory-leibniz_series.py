"""
 Geometry - Pi Gregory-Leibniz Series 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Geometry - Pi Gregory-Leibniz Series"
__author = "laffra"

def __algorithm():
    from decimal import Decimal

    # Calculate Pi using Gregory-Leibniz Series:
    #
    #  pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ....
    #
    def calculatePi(steps):
        pi = 1
        for k in range(3, 2 * steps, 4):
            pi -= Decimal(1)/k
            pi += Decimal(1)/(k+2)
        return pi * 4

    print('''
    PI = %s

    In Carl Sagan's novel "Contact", when listing Pi in base 11,
    a circle could be seen inside Pi. This fact never made it to
    the movie.
    ''' % calculatePi(1000))

def __visualization():
    import math
    
    error = pi * 4 - Decimal(math.pi)

    text(50, 50, 'step = %d of %d' % (k/2 + 1, steps), 25)
    text(50, 80, 'pi = %.25f' % (pi * 4), 25)
    text(50, 110, 'PI = %.25f' % math.pi, 25)
    text(50, 140, 'Error = %.25f' % error, 25)

    rect(50, 200, 500, 200)
    line(50, 300, 550, 300)

    line(300, 270, 300, 310)
    text(285, 270, "PI", 32)

    x = int(300 + error * 1000)
    line(x, 290, x, 310, 'red')
    text(x - 10, 340, "pi", 32, color='red')