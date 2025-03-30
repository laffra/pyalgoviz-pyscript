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
__author = "chris@chrislaffra.com"

def __algorithm():
    import random
    import math

    inside = []
    outside = []
    total = 500

    for i in range(total):
        x, y = (random.random() * 2) - 1, (random.random() * 2) - 1
        (inside if math.sqrt(x**2 + y**2) < 1.0 else outside).append((x,y))
        pi = (float(len(inside)) / total) * 4

    print("At position 17,387,594,880 of Pi you find the sequence 0123456789.")
    print(f"PI={pi}") 

def __visualization():
    if __lineno__ > 12:
        circle(300, 223, 220)
        for x,y in inside:
            circle(300 + x * 220, 223 + y * 220, 5, "green")
        for x,y in outside:
            circle(300 + x * 220, 223 + y * 220, 5, "red")
        text(145, 500, "PI=%.10f" % pi, size=25)
    else:
        text(145, 250, "Dart %d/%d" % (i, total), size=25)
        if __lineno__ == 9 and i % 50 == 0: beep(200 + i * 4, 2000)
