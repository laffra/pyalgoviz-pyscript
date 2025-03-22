"""
 Numbers - Prime Generator - 6 - DP 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Numbers - Prime Generator - 6 - DP"
__author = "chris@chrislaffra.com"

def __algorithm():
    import time, math

    def getPrimes(count=50):
        primes = [2]
        yield 2
        n = 3
        while n < count:
            for factor in filter(lambda k: k<=int(math.sqrt(n)), primes):
                if n % factor == 0: break
            else:
                primes.append(n)
                yield n        
            n += 2

    start = time.time()

    for p in getPrimes():
        print(p,)
    
    end = time.time()

    print('This took', end - start, 'seconds')

def __visualization():
    X, Y, D = 100, 130, 40

    def drawGrid():
        for y in range(10):
            for x in range(10):
                number = y*10+x+1
                if number >= n:
                    return
                color = 'lightyellow' if number<=n else '#ccc'
                color = 'pink' if number in primes else color
                rect(X+x*D, Y+y*D, D-5, D-5, color)
                text(X+x*D+2, Y+y*D+D/2, number, 15)
            
    def drawLabel(y, s):
        rect(X, y, 395, 40, '#333')
        text(X+30, y+30, s, 30, color='lightblue')
    
    drawGrid()         
    drawLabel(Y-70, 'Primes to 50 - DP')
    if __lineno__ == 22:
        drawLabel(Y+230, 'Algorithm took %.2f sec.' % (end-start))