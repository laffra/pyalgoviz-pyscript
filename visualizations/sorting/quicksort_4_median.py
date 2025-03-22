"""
 Sorting - QuickSort - 4 - Median 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Sorting - QuickSort - 4 - Median"
__author = "chris@chrislaffra.com"

def __algorithm():
    import random

    def qsort(array):
        if len(array) < 2: return array
        pivot = (array[0] + array[len(array)//2] + array[-1])//3
        less = list(filter(lambda n: n<pivot, array))
        equal = list(filter(lambda n: n==pivot, array))
        larger = list(filter(lambda n: n>pivot, array))
        return qsort(less) + equal + qsort(larger)

    array = qsort(random.sample(range(40), 40))

    print(array)

    # See: http://en.wikipedia.org/wiki/Quicksort
    #
    # Worst case performance        O(n2) (extremely rare)
    # Best case performance            O(n log n)
    # Average case performance        O(n log n)
    # Worst case space complexity    O(n) (naive)
    #                                 O(log n) (Sedgewick 1978)

def __visualization():
    highlight = -1 if __lineno__ > 11 else array.index(pivot)
    barchart(10, 20, 510, 90, array, highlight=highlight, scale=2)
    text(85, 130, 'QuickSort using the median pivot (Sedgewick)', 16, color="teal")