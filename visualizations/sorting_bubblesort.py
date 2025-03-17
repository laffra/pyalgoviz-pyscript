"""
 Sorting - BubbleSort 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Sorting - BubbleSort"
__author = "laffra"

def __algorithm():
    def bubbleSort(L):
        for i in range(len(L)-1, 0, -1): 
            for j in range(i):
                if L[j]>L[j+1]:
                    L[j],L[j+1] = L[j+1],L[j]
            
    from random import sample
    data = sample(range(30), 30)

    bubbleSort(data)

    # See: http://en.wikipedia.org/wiki/Bubble_sort
    # 
    # Worst case performance        O(n^2)
    # Best case performance            O(n)
    # Average case performance        O(n^2)
    # Worst case space complexity    O(1)

def __visualization():
    barchart(50, 60, 460, 150, data, highlight=i, scale=4)

    def show(name, index, y, color):
        x = 53+index*460/len(data)
        line(x, y, x, 215, color, 2)
        text(x+3, y+3, '%s = %d' % (name, index), 20)

    show('i', i, 250, 'red')
    show('j', j, 290, 'blue')

    rect(35, 330, 490, 40, '#333')
    text(200, 360, 'Bubble Sort', 30, color='lightblue')