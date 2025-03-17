"""
 Numbers - Fibonacci / Golden Ratio 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

name = " Numbers - Fibonacci / Golden Ratio "
author = " laffra "

def algorithm():
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
    
    print('The first %d numbers in the Fibonacci sequence: ' % len(numbers))
    print(numbers)
    
     