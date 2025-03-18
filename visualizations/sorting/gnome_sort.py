"""
 Sorting - Gnome Sort 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Sorting - Gnome Sort"
__author = "laffra"

def __algorithm():
    def kabouterSort(s):
        for i in range(1, len(s)): 
            for j in range(i, 0, -1):
                if s[j-1] > s[j]:
                    s[j-1], s[j] = s[j], s[j-1] 

    data = [
       24, 30, 20, 15, 25, 1, 8, 7, 37, 16,  21, 2, 12, 22, 34, 
       33, 14, 38, 39, 18, 36, 28, 17, 4, 32, 13, 40, 35, 6, 5
    ]

    kabouterSort(data)

    # See: http://en.wikipedia.org/wiki/Gnome_sort
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

    show('i', i, 320, 'red')
    show('j', j, 360, 'blue')

    beep(200 + i * 50, 200)
    beep(j * 100, 10)