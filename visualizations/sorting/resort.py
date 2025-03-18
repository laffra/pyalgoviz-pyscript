"""
 Sorting - ReSort 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Sorting - ReSort"
__author = "mhcoma"

def __algorithm():
    def reSort(a):
        size = len(a)
        for h in range(2):
            for i in range(size-1, 0, -1):
                for j in range(0, (i//2)+1):
                    if a[j] > a[i-j]:
                        a[j], a[i-j] = a[i-j], a[j]
                k = 0
                for s in range(i, size-1-((size-1-i)//2)):
                    if a[s] > a[size-1-k]:
                        a[s], a[size-1-k] = a[size-1-k], a[s]
                    k += 1
        return a

    data = [
       24, 30, 20, 15, 25, 1, 8, 7, 37, 16, 
       21, 2, 12, 22, 34, 33, 14, 38, 39, 18, 
       36, 28, 17, 4, 32, 13, 40, 35, 6, 5, 
       11, 31, 26, 27, 23, 29, 19, 10, 3, 9
    ]

    reSort(data)

    # case performance        O((n^2)*2)

def __visualization():
    #
    #  visualize the above list as a barchart, while being sorted
    #  

    barchart(50, 25, 480, 400, data, highlight=i, scale=10)

    beep(i * 100, 50)