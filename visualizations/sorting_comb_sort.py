"""
 Sorting - Comb Sort 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Sorting - Comb Sort"
__author = "laffra"

def __algorithm():
    def combSort(input):
        gap = len(input)
        swaps = True
        while gap > 1 or swaps:
            gap = max(1, int(gap / 1.25))  # minimum gap is 1
            swaps = False
            for i in range(len(input) - gap):
                j = i+gap
                if input[i] > input[j]:
                    input[i], input[j] = input[j], input[i]
                    swaps = True

    data = [
       24, 30, 20, 15, 25, 1, 8, 7, 37, 16, 
       21, 2, 12, 22, 34, 33, 14, 38, 39, 18, 
       36, 28, 17, 4, 32, 13, 40, 35, 6, 5, 
       11, 31, 26, 27, 23, 29, 19, 10, 3, 9
    ]

    combSort(data)

    # See: http://en.wikipedia.org/wiki/Comb_sort2
    #
    # Worst case performance        O(n^2)[1]
    # Best case performance            O(n)
    # Average case performance        O(n^2/2^p), p the number of increments[1]
    # Worst case space complexity    O(1)

def __visualization():
    #
    #  visualize the above list as a barchart, while being sorted
    #  

    barchart(50, 70, 500, 300, data, highlight=i, scale=7)

    beep(i * 100, 50)