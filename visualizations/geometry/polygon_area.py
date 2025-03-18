"""
 Polygon Area 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Polygon Area"
__author = "KingRobertKing"

def __algorithm():
    # remarkably the parallelograms cancel each other out giving
    # the area of the polygon!
    # polygon points in clockwise order
    points = [
        (10, 30), (200, 10), (215, 30), (208, 70), (185, 75), 
        (150, 130), (160, 190), (320, 40), (320, 80), (120, 290)
    ]

    def cross(line1, line2):
        assert line1[0] == line2[0]
        x1 = line1[0][0] - line1[1][0]
        y1 = line1[0][1] - line1[1][1]
        x2 = line2[0][0] - line2[1][0]
        y2 = line2[0][1] - line2[1][1]
        return x1 * y2 - x2 * y1

    def vector(p1, p2):
        return p1, p2

    parallelograms = []
    area = 0
    point0 = points[0]
    for point1, point2 in zip(points[1:], points[2:]):
        line1 = vector(point0, point1)
        line2 = vector(point0, point2)
        parallelogram = cross(line1, line2)/2.0
        parallelograms.append(parallelogram)
        area = abs(sum(parallelograms))

    print(area)

    #http://www.topcoder.com/tc?d1=tutorials&d2=geometry1&module=Static

def __visualization():
    text(20, 385, str(parallelograms), size=23, font='Arial', color='black')
    text(20, 435, "Polygon Area: %d" % area, size=43, font='Arial', color='black')
    circle(point0[0], point0[1], 15, fill='pink', border='black')

    def draw_polygon():
        for (x1, y1), (x2, y2) in zip(points, points[1:] + [points[0]]):
            line(x1, y1, x2, y2, color='black', width=1)

    draw_polygon()

    x1, y1 = point1
    circle(x1, y1, 15, fill='yellow', border='black')
    x2, y2 = point2
    circle(x2, y2, 15, fill='blue', border='black')

    x0, y0 = point0

    line(x0, y0, x1, y1, color='red', width=6)
    line(x0, y0, x2, y2, color='red', width=6)

    x3 = (x1 + x2) - x0
    y3 = (y1 + y2) - y0
    text((x1 + x2)/2 - 50 + 50, (y1 + y2)/2 + 50,
        parallelogram, size=33, font='Arial', color='black')
    circle(x3, y3, 15, fill='pink', border='black')
    line(x3, y3, x1, y1, color='red', width=6)
    line(x3, y3, x2, y2, color='red', width=6)

    line(x1, y1, x2, y2, color='orange', width=6)
