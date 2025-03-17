"""
 Numbers - Fibonacci / Golden Ratio 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Numbers - Fibonacci / Golden Ratio"
__author = "laffra"

def __algorithm():
    def fibonacci():
        previous,current = 1,1
        yield previous
        yield current
        while 1:
            current,previous = previous+current, current
            yield current

        
    numbers = []
    fib = fibonacci()
    for n in range(50):
        numbers.append(next(fib))
    
    print('The first %d numbers in the Fibonacci sequence:' % len(numbers))
    print(numbers)

def __visualization():
    from math import pi

    R,U,L,D = A = range(4)
    dir,angle,x,y = D,pi,150,170
    scale = min(10.0, 60.0/sum(numbers))
    w = [10*n*scale for n in numbers]
    for k in range(len(numbers)):
        ax, ay = 0, 0
        if k == 0:
            x += w[k]; ax,ay = x+w[k],y
        elif k == 1:
            x += w[k]; ax,ay = x,y
        else:
            if dir == R:
                x += w[k-1]; y -= w[k-2]; ax,ay = x,y
            elif dir == U:
                x -= w[k-2]; y -= w[k]; ax,ay = x,y+w[k] 
            elif dir == L:
                x -= w[k]; ax,ay = x+w[k],y+w[k]
            elif dir == D:
                y += w[k-1]; ax,ay = x+w[k],y
        if w[k]>5:
            rect(x, y, w[k], w[k], border='#CCC')
            text(x+1, y+9, numbers[k], 10, 'Arial', '#CCC')
            arc(ax, ay, w[k]-3, w[k], angle, angle+pi/1.95, 'red')
        angle -= pi/2
        dir = A[(dir+1)%4]
    
    rect(35, 370, 400, 50, '#444')
    text(115, 405, 'The Golden Ratio', 30, 'Arial', 'gold')
    text(135, 60, 'O = %.10f' % (float(numbers[-1])/numbers[-2]), 30)
    text(142, 58, '|', 36)

    y = 50
    for n,p in enumerate(reversed(numbers)):
        size = max(1, 20 - n/1.5)
        text(470, y, p, size=size)
        y += size + 2
    
    beep(len(numbers)*30, 3000)