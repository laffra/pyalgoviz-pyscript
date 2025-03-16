"""
Bubble Sort visualization
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

from . import barchart, text, line, rect

NAME = "Bubble Sort"
AUTHOR = "Chris Laffra"


def algorithm():
    """
    Sort a list of numbers using the Bubble Sort algorithm.
    """
    from random import sample

    def bubble_sort(L):
        for i in range(len(L)-1, 0, -1):
            for j in range(i):
                if L[j]>L[j+1]:
                    L[j],L[j+1] = L[j+1],L[j]

    data = sample(range(30), 30)
    bubble_sort(data)

    # See: http://en.wikipedia.org/wiki/Bubble_sort

    # Worst case performance		O(n^2)
    # Best case performance			O(n)
    # Average case performance		O(n^2)
    # Worst case space complexity	O(1)


def visualization():
    barchart(50, 120, 620, 150, data, highlight=i, scale=4)

    def show(name, index, y, color):
        x = 53+index*460/len(data)
        line(x, y, x, 270, color, 2)
        text(x+3, y+3, f'{name} = {index}', 20)

    show('i', i, 350, 'red')
    show('j', j, 390, 'blue')

    rect(50, 30, 620, 40, '#333')
    text(250, 60, 'Bubble Sort', 30, color='lightblue')
