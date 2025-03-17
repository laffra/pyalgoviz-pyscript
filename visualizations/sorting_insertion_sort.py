"""
 Sorting - Insertion Sort 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Sorting - Insertion Sort"
__author = "laffra"

def __algorithm():
    def insertionSort(s):
        for i in range(1, len(s)):
            val = s[i]
            j = i - 1
            while (j >= 0) and (s[j] > val):
                s[j+1] = s[j]
                j = j - 1
            s[j+1] = val

    data = [
       24, 30, 20, 15, 25, 1, 8, 7, 37, 16, 
       21, 2, 12, 22, 34, 33, 14, 38, 39, 18, 
       36, 28, 17, 4, 32, 13, 40, 35, 6, 5, 
    ]
         
    insertionSort(data)
    print(data)

    # See: http://en.wikipedia.org/wiki/Insertion_sort
    #
    # Worst case performance        О(n2) comparisons, swaps
    # Best case performance            O(n) comparisons, O(1) swaps
    # Average case performance        О(n2) comparisons, swaps
    # Worst case space complexity    О(n) total

def __visualization():
    barchart(10, 20, 500, 140, data, highlight=i, scale=2.5)
    text(530, 40, 'data')

    w = 460/len(data)

    def barX(index):
        return 40+index*w  

    for n in range(len(data)):
        text(barX(n)-4, 180, n)
    
    def show(name, index, y, color):
        x = barX(index)
        line(x, y, x, 185, color, 2)
        text(x+3, y+3, '%s = %d' % (name, index))

    show('i', i, 220, 'blue')
    show('j', j, 260, 'red')

    beep(j * 50, 1000)