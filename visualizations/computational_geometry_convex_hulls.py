"""
 Computational Geometry - Convex Hulls 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Computational Geometry - Convex Hulls"
__author = "ezduanmu"

def __algorithm():
    # Gift Wrapping algorithm aka Jarvis March for Convex hull. http://en.wikipedia.org/wiki/Gift_wrapping_algorithm
    # Most of algo code has been taken from Tom Switzer blog post at http://tomswitzer.net/2009/12/jarvis-march/ . 
    #I liked the way the algo was explained by author and thought this visualization would help anyone learning this algo. 

    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)
 
    def cmp(a, b):
        return (a > b) - (a < b) 
 
    def turn(p, q, r):
        '''Returns -1, 0, 1 if p,q,r forms a right, straight, or left turn.'''
        return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)
 
    def _dist(p, q):
        '''Returns the squared Euclidean distance between p and q.'''
        dx, dy = q[0] - p[0], q[1] - p[1]
        return dx * dx + dy * dy
 
    def _next_hull_pt(points, p):
        '''Returns the next point on the convex hull in CCW from p.'''
        q = p
        for r in points:
            t = turn(p, q, r)
            if t == TURN_RIGHT or t == TURN_NONE and _dist(p, r) > _dist(p, q):
                q = r
        return q
 
    def convex_hull(points):
        '''Returns the points on the convex hull of points in CCW order.'''
        hull = [min(points)]
        for p in hull:
            q = _next_hull_pt(points, p)
            if q != hull[0]:
                hull.append(q)
        return hull

    pos = {
       '1':(0,100), '2':(150,0), '3':(150,180),
       '4':(300,0), '5':(300,200), '6':(450,100),
       '7':(60,90), '8':(50,200), '9':(350,250),
       '10':(250,100), '11':(400,100), '12':(480,160)

    }

    all_points = [pos[str(i+1)] for i in range(len(pos.keys()))]
    convex_hull_points = convex_hull(all_points)
    print(convex_hull_points)

def __visualization():
    rect(100, 22, 500, 40, '#333')
    text(120, 52, 'Jarvis March - Convex Hull', 30, color='lightblue')

    #circles and texts
    for key,value in pos.items():
        x,y = value
        #color = 'blue' if value in convex_hull_points else 'red'
        circle(60+x, 120+y, 20, 'orange')
        text(55+x, 125+y, key, 15)

    #code for drawing the convex hull
    x1,y1 = (0,100)
    for key,value in enumerate(hull,start = 1): 
        x2,y2 = value
        line(60+x1, 120+y1, 60+x2, 120+y2, 'green')
        x1,y1 = x2,y2
        circle(60+x2, 120+y2, 20, 'teal')
        #TODO: should revisit this terrible usage of dictionary look up by values :( # sideaffects_of_coding_at_03am. 
        text(55+x2, 125+y2, list(pos.keys())[list(pos.values()).index((x2,y2))], 15)

    #Connecting last node to first node on convex hull.    
    if __lineno__ > 46 and hull == convex_hull_points:
        line(60+x2, 120+y2, 60+0, 120+100, 'green')