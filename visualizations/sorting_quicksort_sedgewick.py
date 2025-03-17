"""
 Sorting - QuickSort Sedgewick 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Sorting - QuickSort Sedgewick"
__author = "laffra"

def __algorithm():
    def qsort(L):
        if len(L) < 2: return L
        x = (L[0] + L[len(L)//2] + L[-1])//3    # use median pivot
        l = list(filter(lambda y: y <  x, L))
        e = list(filter(lambda y: y == x, L))
        g = list(filter(lambda y: y >  x, L))
        return qsort(l) + e + qsort(g)

    data = [
       24, 30, 20, 15, 25, 1, 8, 7, 37, 16, 
       21, 2, 12, 22, 34, 33, 14, 38, 39, 18, 
       36, 28, 17, 4, 32, 13, 40, 35, 6, 5, 
    ]
         
    import random
    result = qsort(random.sample(range(30), 30))

    # See: http://en.wikipedia.org/wiki/Quicksort
    #
    # Worst case performance        O(n2) (extremely rare)
    # Best case performance            O(n log n)
    # Average case performance        O(n log n)
    # Worst case space complexity    O(n) (naive)
    #                                 O(log n) (Sedgewick 1978)

def __visualization():
    index = data.index(x) if x in data else 0
    barchart(10, 20, 510, 90, data, highlight=index, scale=2)
    text(530, 40, 'data')

    barchart(10, 120, 510, 90, L, scale=2)
    text(530, 150, 'current')

    barchart(10,  220, 220, 90, l, fill='darkgreen', scale=2)
    barchart(240, 220, 50,  90, e, fill='yellow', scale=2)
    barchart(300, 220, 220, 90, g, fill='blue', scale=2)
    text(530, 240, 'next')
    text(245, 325, 'x = %d' % x)

    beep(200 + data.index(x) * 50, 100)

    barchart(10, 340, 510, 90, result, fill='teal', scale=2)
    text(530, 360, 'result')