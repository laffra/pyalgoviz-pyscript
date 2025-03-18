"""
 Dutch national flag problem 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Dutch national flag problem"
__author = "stasiek7776"

def __algorithm():
    def samp(A, mid):
        i = 0
        j = 0
        k = len(A)
        while j < k:
            if A[j] < mid:
                A[i], A[j] = A[j], A[i]
                i = i + 1
                j = j + 1
            elif A[j] > mid:
                k = k - 1
                A[j], A[k] = A[k], A[j]
            else:
                j = j + 1
        
    from random import shuffle
    data = [1,2,3]*10
    shuffle(data)

    samp(data, 2)

    # Insertion sort with n log n behavior invented by Chris Laffra

    # Worst case performance        O(n log n)
    # Best case performance            O(n log n)
    # Average case performance        O(n log n)
    # Worst case space complexity    O(1)

def __visualization():
    barchart(50, 60, 460, 150, data, highlight=j, scale=45)

    beep(mid * 100, 10)

    def show(name, index, y, color):
        x = 53+index*460/len(data)
        line(x, y, x, 215, color, 2)
        text(x+3, y+3, '%s = %d' % (name, index), 20)

    show('j', j, 250, 'red')
    show('i', i, 270, 'teal')
    show('k', k, 290, 'blue')

    rect(35, 330, 490, 40, '#333')
    text(80, 360, 'Dutch national flag problem', 30, color='lightblue')