"""
 Sorting - TimSort 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Sorting - TimSort"
__author = "chris@chrislaffra.com"

def __algorithm():
    def timSort(data):
        data.sort()        # Call TimSort, the Python list.sort

    data = [
       24, 30, 20, 15, 25, 1, 8, 7, 37, 16, 
       21, 2, 12, 22, 34, 33, 14, 38, 39, 18, 
       36, 28, 17, 4, 32, 13, 40, 35, 6, 5, 
    ]

    for n in data:
        print(n,)

    timSort(data)

    for n in data:
        print(n,)

    # See: http://en.wikipedia.org/wiki/Timsort
    #
    # Worst case performance        O(n/log n)[1]
    # Best case performance            O(n)
    # Average case performance        O(n/log n)
    # Worst case space complexity    O(n)

def __visualization():
    barchart(50, 20, 510, 300, data, highlight=data.index(n), scale=6)

    text(120, 350, 'TimSort is the Python built-in list.sort', 22)

    if __lineno__ in [11, 16]: beep(200 + n*100, 50)