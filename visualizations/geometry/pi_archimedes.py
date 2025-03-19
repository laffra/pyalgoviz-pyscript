"""
 Geometry - Pi Archimedes 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Geometry - Pi Archimedes"
__author = "laffra"

def __algorithm():
    import math

    def pi_archimedes(n):
        '''
        See: http://www.craig-wood.com/nick/articles/nick/articles/pi-archimedes/
        An interesting discussion on the approximation algorithm can be found here:
        http://itech.fgcu.edu/faculty/clindsey/mhf4404/archimedes/archimedes.html
        '''
        edge_length_squared = 2.0
        edges = 4
        step = 1
        for i in range(n):
            edge_length_squared = 2 - 2 * math.sqrt(1 - edge_length_squared / 4)
            edges *= 2
            step += 1
        return edges * math.sqrt(edge_length_squared) / 2

    print('''
    PI = %s
    This algorithm is over 2,200 years old

    In 1850, William Shanks took 15 years to estimate
    Pi to 707 digits. Turns out he made an error at 527
    ''' % pi_archimedes(10))

def __visualization():
    cx, cy, r, angle = 450, 270, 200, math.pi/4
    colors = [ 'orange', 'red', 'blue', 'teal' ]
    x1,y1 = cx + r*math.cos(angle), cy - r*math.sin(angle)

    circle(cx, cy, r)
    PI = (edges * math.sqrt(edge_length_squared) / 2)
    text(10, 30, 'Step: %d' % step, 25)
    text(10, 60, 'Number of sides: %d' % edges, 25)

    if __lineno__ >= 15:
        text(10, 90, 'Pi: %s' % PI, 25)
        text(10, 120, 'Error: %.10f' % (math.pi - PI), 25)

    for edge in range(edges+1):
        x2,y2 = cx + r*math.cos(angle), cy - r*math.sin(angle)
        line(x1, y1, x2, y2, colors[step % 4], 3)
        line(cx, cy, x1, y1, '#AAA')
        x1,y1 = x2,y2
        angle += 2*math.pi/edges
    
    beep(step * 300, 10)