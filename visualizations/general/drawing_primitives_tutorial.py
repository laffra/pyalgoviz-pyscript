"""
 Drawing Primitives Tutorial 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Drawing Primitives Tutorial"
__author = "chris@chrislaffra.com"

def __algorithm():
    # generate some numbers for x, y, and n

    for k in range(20):
        for x in range(50, 500, 100):
            for y in range(50, 400, 100):
                n = y // 50

def __visualization():
    # visualize the state, i.e., the values for x, y, and n
    from math import pi

    text(x, y, "x=%s y=%s n=%d" % (x, y, n), size=10 + n*3, font="Arial", color='red')
    rect(450, 50, 50 + n*10, 50 + n*10, fill="brown", border="lightyellow")
    line(50, 50, x, y, color="purple", width=6)
    circle(300, 200, n * 25, fill="transparent", border="green")
    text(50, 450, f"Loop {k+1} of 20")
    arc(100, 325, 30, (n - 1) * 2 * pi/4, n * 2 * pi/4, "orange", 3)

    if __lineno__ == 3:
        beep(500 + k * 50, 1000)

    # Click on the Help button to see all drawing primitives.