"""
 Geometry - Pi Monte Carlo 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Geometry - Pi Monte Carlo"
__author = "laffra"

def __algorithm():
    import random
    import math

    inside = []
    outside = []
    total = 2000

    for i in range(total):
        x = (random.random() * 2) - 1
        y = (random.random() * 2) - 1
        if math.sqrt(x**2 + y**2) < 1.0:
            inside.append((x,y))
        else:
            outside.append((x,y))

        pi = (float(len(inside)) / total) * 4

    print('''
    PI=%s 

    At position 17,387,594,880 of Pi you find the sequence 0123456789.
    ''' % pi)

def __visualization():
    circle(300, 223, 220)

    if __lineno__ > 16:
        for x,y in inside:
            circle(300 + x * 220, 223 + y * 220, 5, "green")
        for x,y in outside:
            circle(300 + x * 220, 223 + y * 220, 5, "red")
    else:
        text(180, 200, "Monte Carlo Estimation", size=25)
        text(145, 250, "Dart %d, PI=%.10f" % (i, pi), size=25)