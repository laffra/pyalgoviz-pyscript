"""
 Sorting - MergeSort 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Sorting - MergeSort"
__author = "chris@chrislaffra.com"

def __algorithm():
    def mergeSort(array, start, end):
        if end - start > 1:
            middle = (start + end) // 2
            mergeSort(array, start, middle)
            mergeSort(array, middle, end)
            merge(array, start, middle, middle, end)

    def merge(array, left, leftEnd, right, rightEnd):
        while left<leftEnd and right<rightEnd:
            if array[left] > array[right]:
                array.insert(left, array.pop(right))
                right += 1
                leftEnd += 1
            else:
                left += 1
            

    import random
    data = random.sample(range(40), 40)
    mergeSort(data, 0, len(data))

    # http://en.wikipedia.org/wiki/Merge_sort

def __visualization():
    barchart(30, 20, 500, 150, data, scale=3)

    def segment(index1, index2, name, color):
        w = min(15, 500/len(data))
        x1, x2 = 10 + index1*w, 10 + index2*w
        if  __lineno__ < 20:
            text(x1-21 if name == 'left' else x2+20, 195, name)
            rect(x1, 180, x2-x1+w, 20, color, color)
    

    segment(right, rightEnd, 'right', 'teal')
    segment(left, leftEnd, 'left', 'orange')