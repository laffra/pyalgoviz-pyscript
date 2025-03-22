"""
 Searching - Binary Search 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Searching - Binary Search"
__author = "chris@chrislaffra.com"

def __algorithm():
    def binary_search(seq, t):
        min = 0; max = len(seq) - 1
        while True:
            if max < min:
                return -1
            mid = (min + max) // 2
            if seq[mid] < t:
                min = mid + 1
            elif seq[mid] > t:
                max = mid - 1
            else:
                return mid

    data = list(range(30))

    for n in [0, 8, 14, 23, 29, -1]:
        checksum = data.index(n) if n in data else -1
        print('binary search for', n, '==>',)
        print(binary_search(data, n), checksum)

def __visualization():
    barchart(10, 10, 500, 150, data, highlight=mid, scale=3)

    text(10, 300, 'running binary search for %d' % t)
    text(10, 330, 'data.index(%d) = %d' % (t, checksum))

    w = 460/len(data)

    def barX(index):
        return 40+index*w  

    for n in range(len(data)):
        text(barX(n)-4, 180, n)
    
    def show(name, index, y, color):
        x = barX(index)
        line(x, y, x, 185, color, 2)
        text(x+3, y+3, '%s = %d' % (name, index))

    rect(barX(min), 190, barX(max)-barX(min), 15, '#EFEFEF', '#EFEFEF')
    found = 'Found the target at index' if mid == checksum else 'mid'
    show('min', min, 220, 'blue')
    show(found, mid, 240, 'orange')
    show('max', max, 260, 'red')

    beep(mid * 100, 50)