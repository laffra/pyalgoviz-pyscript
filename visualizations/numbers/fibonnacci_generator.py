"""
 Numbers - Fibonnacci Generator 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Numbers - Fibonnacci Generator"
__author = "kalyan359"

def __algorithm():
    def fib(count = 50):    # write Fibonacci series up to n
        fib_list = []
        a, b = 0, 1
        while a < count:
            fib_list.append(a)
            a, b = b, a+b
        return fib_list

    fib_list = fib()
    print(fib_list)

def __visualization():
    X, Y, D = 100, 150, 40

    def drawGrid():
        for y in range(10):
            for x in range(10):
                number = y*10+x
                if number >= 50:
                    return
                color = 'orange' if number<=a else '#ccc'
                color = 'teal' if number in fib_list else color
                rect(X+x*D, Y+y*D, D-5, D-5, color)
                text(X+x*D+2, Y+y*D+D/2, number, 15)
            
    rect(X, 72, 395, 40, '#333')
    text(X+15, 102, 'Fibonacci Series Generator', 30, color='lightblue')
    drawGrid()
    beep(200 + a * 100, 200)