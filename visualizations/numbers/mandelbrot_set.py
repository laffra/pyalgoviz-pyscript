"""
 Numbers - Mandelbrot Set 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Numbers - Mandelbrot Set"
__author = "laffra"

def __algorithm():
    ITERATIONS,W,H = 9,20,20

    def mandelbrot(x1, x2, y1, y2, iterations):
        img = [[-1]*W for _ in range(H)]
        px, py = (x2-x1)/W, (y2-y1)/H
        for x in range(W):
            real = x1 + x * px
            for y in range(H):
                imag = y1 + y * py
                c,z = complex(real, imag), 0.0j
                for i in range(iterations):
                    z = z*z + c
                    if (z.real*z.real + z.imag*z.imag) >= 4:
                        color = i
                        break
                else:
                    color = iterations
                img[y][x] = color
        return img

    # See http://nbviewer.ipython.org/f5707335f40af9463c43
    image = mandelbrot(-2.0, 1.0, -1.0, 1.0, 10)

def __visualization():
    if __lineno__ == 22:
    
        D = 400/W
    
        rect(0,0,600,600,"black")

        for y,row in enumerate(image):
            for x,color in enumerate(row):
                r = color * 256/18
                g = color * 256/12
                b = color * 256/4
                rect(100+x*D, 22+y*D, D, D, 'rgb(%d,%d,%d)' % (r,g,b))