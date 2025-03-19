"""
 Sorting - Heap Sort 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Sorting - Heap Sort"
__author = "laffra"

def __algorithm():
    from heapq import heappush, heappop

    def makeHeap(iterable):
        heap = [] 
        for value in iterable:
            heappush(heap, value)
        return heap
        
    numbers = [
       15,25,1,8,7,16,21,2,4,13,6,5,12,22,34,14,18,28,24,20,17
    ]
    heap = makeHeap(numbers)
    result = []
    while heap:
        result.append(heappop(heap))

def __visualization():
    barchart(20, 20, 500, 110, numbers, scale=2)
    text(200, 150, 'Unordered List of Tasks')

    if heap:
        rect(20, 180, 500, 230)
        text(200, 400, 'Temporary Binary Min-Heap')
        prev_start, prev_count = 0,1
        for level in range(0, 1 + int(math.log(len(heap), 2))):
            y = 220 + level * 35
            start, count = 2**level-1, 2**level
            for n in range(start, start+count):
                x = 20 + (n-start+1) * 500/(count+1)
                p = prev_start + (n-start) // 2
                px = 20 + (p-prev_start+1) * 500/(prev_count+1)
                color = 'salmon' if heap[n] == value else 'lightblue' 
                if level > 0: line(x, y, px, y-32, 'orange')
                rect(x-9, y-13, 25, 15, color)
                text(x, y, heap[n])
            prev_start, prev_count = start, count
    else:
        barchart(20, 200, 500, 110, result, scale=2)
        text(220, 330, 'Sorted Result')