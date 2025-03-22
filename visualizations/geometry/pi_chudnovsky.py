"""
 Geometry - Pi Chudnovsky 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Geometry - Pi Chudnovsky"
__author = "chris@chrislaffra.com"

def __algorithm():
    from decimal import Decimal, getcontext
    from math import factorial

    getcontext().prec = 25

    def calculatePi(n): 
        pi = Decimal(0)
        k = 0
        while k < n:
            pi += (
                (Decimal(-1)**k) * 
                (Decimal(factorial(6*k)) /
                    ((factorial(k)**3)*(factorial(3*k))) * 
                    (13591409+545140134*k) /
                    (640320**(3*k))
                )
            )
            k += 1
        return (pi * Decimal(10005).sqrt()/4270934400)**(-1)

    print('''
    PI = %s

    In 2016, Pi was calculated to 22.4 trillion digits."
    ''' % calculatePi(10))

def __visualization():
    beep(__lineno__*200, 1000)

    from decimal import Decimal

    PI = pi * Decimal(10005).sqrt()/4270934400
    PI = PI**(-1)

    text(50, 60, 'Step = %d' % k, 25)
    text(50, 100, 'PI = %.25f' % PI, 25)
    text(50, 140, 'Error = %.25f' % (PI - Decimal(math.pi)), 25)