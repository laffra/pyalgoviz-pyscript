"""
 Trigonometry - Sin/Cos/Tan 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Trigonometry - Sin/Cos/Tan"
__author = "laffra"

def __algorithm():
    import math 

    def getPoints(scale=30):
        points = []
        for r in range(-scale, 2*scale+1):
            x = r/float(scale)
            sin = math.sin(r*math.pi/scale)
            cos = math.cos(r*math.pi/scale)
            tan = math.tan(r*math.pi/scale)  # which really is sin/cos
            points.append((x, sin, cos, tan))
        return points

    print(getPoints(13))

def __visualization():
    X,W = 250,200
    Y,H = 250,200

    x = lambda v: X + (v*W/2)
    y = lambda v: Y - (v*H/2)

    for n in range(len(points)-1):
        x1,s1,c1,t1 = points[n]
        x2,s2,c2,t2 = points[n+1]
        line(x(x1), y(s1), x(x2), y(s2), 'blue', 2)
        line(x(x1), y(c1), x(x2), y(c2), 'red', 2)
        line(x(x1), y(t1), x(x2), y(t2), 'green', 2)
        beep(abs(y(t1)*10), 100)
    
    x1,s1,c1,t1 = points[-1]
    text(x(x1)-43, y(s1)+5, 'sin', 25, 'Arial', 'blue')
    text(x(x1)-43, y(c1)+5, 'cos', 25, 'Arial', 'red')

    x1,s1,c1,t1 = points[-1]
    text(x(x1)+7, y(t1)+5, 'tan', 25, 'Arial', 'green')

    line(X-W, Y, X+W, Y, '#CCC')
    line(X, Y-H, X, Y+H, '#CCC')