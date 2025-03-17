"""
 Sorting - QuickSort - 5 - No Recursion 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Sorting - QuickSort - 5 - No Recursion"
__author = "laffra"

def __algorithm():
    import random

    def qsort(array):
        work = [array]
        result = []
        while work:
            array = work.pop(0)
            if len(array) < 2:
                result.extend(array)
            else:
                pivot = array[0]
                work = [
                    list(filter(lambda n: n<pivot, array)),
                    list(filter(lambda n: n==pivot, array)),
                    list(filter(lambda n: n>pivot, array)),
                ] + work
        return result

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
    text(145, 130, 'QuickSort without using recursion', 16, color="teal")