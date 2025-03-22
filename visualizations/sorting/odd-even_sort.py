"""
 Sorting - Odd-Even Sort 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Sorting - Odd-Even Sort"
__author = "chris@chrislaffra.com"

def __algorithm():
    def oddEvenSort(a):
        swapped = 0
        while swapped != -1:
            swapped = -1
            for odd in (1,0):
                for n in range(odd, len(a)-1, 2):
                    if a[n] > a[n+1]:
                        a[n+1], a[n] = a[n], a[n+1]
                        swapped = n;

    from random import shuffle
    data = list(range(30))
    shuffle(data)
    oddEvenSort(data)

    # See: http://en.wikipedia.org/wiki/Odd-even_sort
    #
    # Worst case performance        O(n^2)
    # Best case performance            O(n)
    # Average case performance        O(n^2)
    # Worst case space complexity    O(1)

def __visualization():
    barchart(10, 10, 500, 150, data, highlight=swapped+1, scale=3)

    w = 460 / len(data)
    x = 40 + w*n
    line(x, 200, x, 165, 'orange' if odd else 'blue', 3)
    text(x+3, 203, '%s = %d' % ('odd' if odd else 'even', n))

    beep(data[swapped] * 100, 50)
    beep(swapped * 100, 50)