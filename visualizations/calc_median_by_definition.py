"""
 calc_median_by_definition 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "calc_median_by_definition"
__author = "WangYe.Hope"

def __algorithm():
    nums = [15,25,1,8,7,16,21,2,4,13,6,5,12,22,34,14,18,28,24,20,17]
    n = len(nums)
    k = 11
    ret = []
    def partition(res, low, high):
        i = (low - 1)  # 最小元素索引
        pivot = res[high]

        for j in range(low, high):
            if res[j] <= pivot:
                i = i + 1
                res[i], res[j] = res[j], res[i]

        res[i + 1], res[high] = res[high], res[i + 1]
        return (i + 1)


    def quickSort(res, low, high):
        if low < high:
            pi = partition(res, low, high)

            quickSort(res, low, pi - 1)
            quickSort(res, pi + 1, high)

    for ni in range(k-1, n):
        buffer = nums[ni - k + 1:ni + 1]
        res = []
        for nj in range(k):
            res.append(buffer[nj])
        quickSort(res,0,len(res)-1)
        l = len(res)
        print(res)
        if l & 1:
            ret.append(res[l//2])
        else:
            ret.append((res[l//2-1]+res[l//2])/2.0)

def __visualization():
    box_width = 23
    box_height = 20

    def box_text(x, y, c, color):
        rect(x, y, box_width, box_height, fill=color)
        text(x + 6, y + 14, c)

    def array_print(dataset, location, color_func=lambda x: 'white'):
        for i, c in enumerate(dataset):
            box_text(i * box_width + 85, location + 10, 
                     c, color_func(i))


    text(50, 90, "SAMPLES")

    array_print(nums, 85, lambda x: 'white' if x != ni else 'red')
    text(50, 135, 'BUFFER')
    array_print(res, 130, lambda x: 'white' if x != ((k-1)/2) and k != (k/2) else 'green')
    text(50, 180, 'RESULTS')
    array_print(ret, 175, lambda x: 'white')