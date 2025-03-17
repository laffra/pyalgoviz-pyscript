"""
 Sorting - Cocktail Sort2 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Sorting - Cocktail Sort2"
__author = "adamklein"

def __algorithm():
    def cocktailSort(A):
        j = 0
        for k in range(len(A)-1, 0, -1):
            swapped = False
            for i in range(k, j, -1):
                if A[i]<A[i-1]:
                    A[i], A[i-1] = A[i-1], A[i]
                    swapped = True
            for i in range(j, k):
                if A[i] > A[i+1]:
                    A[i], A[i+1] = A[i+1], A[i]
                    swapped = True
            if not swapped:
                return A
            j += 1
        
    data = [
       24, 30, 20, 15, 25, 1, 8, 7, 37, 16,  21, 2, 12, 22, 34, 
       33, 14, 38, 39, 18, 36, 28, 17, 4, 32, 13, 40, 35, 6, 5
    ]
    cocktailSort(data)

    # See: http://en.wikipedia.org/wiki/Cocktail_sort
    #
    # Worst case performance        O(n^2)
    # Best case performance            O(n)
    # Average case performance        O(n^2)
    # Worst case space complexity    O(1)

def __visualization():
    barchart(10, 10, 500, 150, data, highlight=i, scale=3)

    w = 460/len(data)

    def barX(index):
        return 40+index*w  

    for n in range(len(data)):
        text(barX(n)-4, 180, n)
    
    def show(name, index, y, color):
        x = barX(index)
        line(x, y, x, 185, color, 2)
        text(x+3, y+3, '%s = %d' % (name, index))
        line(x-15, y+5, x-15, y-3, color, 2)
        line(x-18, y+5, x-12, y+5, color, 2)
        line(x-20, y-10, x-15, y-3, color, 2)
        line(x-10, y-10, x-15, y-3, color, 2)
        line(x-20, y-9, x-10, y-9, color, 1)

    show('i', i, 320, 'blue')
    beep(i * 100, 50)
    show('k', k, 360, 'red')
    beep(i * 100, 50)
    show('j', j, 360, 'green')