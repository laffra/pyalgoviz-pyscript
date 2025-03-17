"""
 Sorting - QuickSort 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Sorting - QuickSort"
__author = "laffra"

def __algorithm():
    import random

    def qsort(array):
        if len(array) < 2: return array
        pivot = array[0]
        less = list(filter(lambda n: n<pivot, array))
        equal = list(list(filter(lambda n: n==pivot, array)))
        larger = list(filter(lambda n: n>pivot, array))
        return qsort(less) + equal + qsort(larger)

    data = random.sample(range(40), 40)
    data = qsort(data)
    print(data)

    # See: http://en.wikipedia.org/wiki/Quicksort
    #
    # Worst case performance        O(n2) (extremely rare)
    # Best case performance            O(n log n)
    # Average case performance        O(n log n)
    # Worst case space complexity    O(n) (naive)
    #                                 O(log n) (Sedgewick 1978)

def __visualization():
    barchart(10, 20, 510, 90, data, highlight=data.index(pivot), scale=2)
    text(530, 40, 'data')

    barchart(10, 120, 510, 90, array, scale=2)
    text(530, 150, 'current')

    barchart(10,  220, 220, 90, less, fill='darkgreen', scale=2)
    barchart(240, 220, 50,  90, equal, fill='yellow', scale=2)
    barchart(300, 220, 220, 90, larger, fill='blue', scale=2)
    text(530, 240, 'next')
    text(245, 330, 'pivot = %d' % pivot, 16, color="teal")

    duration = end - start
    text(45, 330, 'Algorithm took %.2fs' % duration, 16, color="teal")