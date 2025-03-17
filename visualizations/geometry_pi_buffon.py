"""
 Geometry - Pi Buffon 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Geometry - Pi Buffon"
__author = "laffra"

def __algorithm():
    from random import randint
    from math import pi, sin, cos

    W = 400        # surface width
    H = 400     # surface height
    D = 25        # half length of each needle
    L = 100     # 2X needle length

    needles = []
    touching = []

    for n in range(1200):
        x,y,a = randint(0,W), randint(0,H), randint(0,200)*pi/100
        x1,y1,x2,y2 = x-D*sin(a), y-D*cos(a), x+D*sin(a), y+D*cos(a)
        needles.append((x1,y1,x2,y2))
        if min(x1,x2)%L>=2*D and max(x1,x2)%L<=2*D:
            touching.append((x1,y1,x2,y2))

    PI = 1.0*len(needles)/len(touching)
    print(len(needles), len(touching), PI)

    print('''
    In 2005, Chao Lu recited 67,890 digits of Pi from memory.
    How many digits do you know from memory?
    ''')

def __visualization():
    beep(__lineno__*100, 1000)

    text(W+45, 50, '%d random needles' % len(needles))
    text(W+45, 70, '%d touching' % len(touching))
    
    rect(W+35, 270, 140, 70, 'black')
    text(W+55, 300, 'Buffon\'s', 25, 'Arial', 'lavender')
    text(W+55, 330, 'Needles', 25, 'Arial', 'lavender')

    text(W+45, 200, 'PI = %s' % PI, 15)

    rect(25, 25, W, H)

    for x in range(0, W, L):
        line(x+25, 0+25, x+25, H+25, '#AAA')
    
    for x1,y1,x2,y2 in needles:
        color = 'red' if (x1,y1,x2,y2) in touching else 'green'
        line(x1+25,y1+25,x2+25,y2+25, color, 1)