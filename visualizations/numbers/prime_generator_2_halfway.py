"""
 Numbers - Prime Generator - 2 - Halfway 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Numbers - Prime Generator - 2 - Halfway"
__author = "laffra"

def __algorithm():
    import time
    start = time.time()

    def isPrime(n):
        for factor in range(2, n//2 + 1):
            if n % factor == 0:
                return False
        return n>1

    primes = []
    for n in range(1, 51):
        if isPrime(n):
            primes.append(n)
        
    print(primes)
    end = time.time()
    print('This took', end - start, 'seconds')

def __visualization():
    X, Y, D = 100, 130, 40

    def drawGrid():
        for y in range(10):
            for x in range(10):
                number = y*10+x+1
                if number > n:
                    return
                color = 'lightyellow' if number<=n else '#ccc'
                color = 'pink' if number in primes else color
                rect(X+x*D, Y+y*D, D-5, D-5, color)
                text(X+x*D+2, Y+y*D+D/2, number, 15)
            
    def drawLabel(y, s):
        rect(X, y, 395, 40, '#333')
        text(X+30, y+30, s, 30, color='lightblue')
    
    drawGrid()         
    drawLabel(Y-70, 'Primes to 50 - Halfway')
    drawLabel(Y+230, 'Algorithm took %.2f sec.' % (end-start))