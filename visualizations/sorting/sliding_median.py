"""
 sliding median 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "sliding median"
__author = "WangYe.Hope"

def __algorithm():
    import heapq

    def move(h1, h2):
        x, i = heapq.heappop(h1)
        heapq.heappush(h2, (-x, i))


    def get_med(h1, h2, k):
        return h2[0][0] * 1. if k & 1 else (h2[0][0] - h1[0][0]) // 2.

    nums = [15,25,1,8,7,16,21,2,4,13,6,5,12,22,34,14,18,28,24,20,17]
    k = 11
    start = False

    #def calc_median_sliding_window(nums, k):
    small, large = [], []
    for ni, x in enumerate(nums[:k]):
        heapq.heappush(small, (-x, ni))
    for _ in range(k - (k >> 1)):
        move(small, large)
    ans = [get_med(small, large, k)]

    start = True
    for ni, x in enumerate(nums[k:]):
        if x >= large[0][0]:
            heapq.heappush(large, (x, ni + k))
            if nums[ni] <= large[0][0]:
                move(large, small)
        else:
            heapq.heappush(small, (-x, ni + k))
            if nums[ni] >= large[0][0]:
                move(small, large)
        while small and small[0][1] <= ni:
            heapq.heappop(small)
        while large and large[0][1] <= ni:
            heapq.heappop(large)
        ans.append(get_med(small, large, k))


    # calc_median_sliding_window(nums,11)

def __visualization():
    box_width = 23
    box_height = 20


    def box_text(x, y, c, color):
        rect(x, y, box_width, box_height, fill=color)
        text(x + 6, y + 14, c)

    def array_print(dataset, location, color_func=lambda x: 'white'):
        for i, c in enumerate(dataset):
            box_text(i * box_width + 80, location + 10, 
                     c, color_func(i))
        
    def box_text2(x, y, c, color):
        rect(x, y, box_width * 1.5, box_height, fill=color)
        text(x + 6, y + 14, c)
    
    def result_print(dataset, location, color_func=lambda x: 'white'):
        for i, c in enumerate(dataset):
            #print(c)
            box_text2(i * box_width * 1.5 + 60, location + 10, 
                     c, color_func(i))
        
    def heap_print(heap, location, color_func=lambda x: 'white', sign=1):
        for i, c in enumerate(heap):
            box_text(i * box_width + 80, location + 10, 
                     c[0] * sign, color_func(i))

    def get_color(x,start,i,k):
        if not start:
            if x == i: return 'red'
            else: return 'white'
        else:
            if x == i+k: return 'red'
            else: return 'white'
        

        

    text(25, 90, "SAMPLES")
    array_print(nums, 85, lambda x: get_color(x,start,ni,k))
    text(25, 135, 'HEAP_SMALL')
    heap_print(small, 130, lambda x: 'white', sign=-1)
    text(25, 180, 'HEAP_LARGE')
    heap_print(large, 185, lambda x: 'white')
    if k & 1:
        text(25, 240, 'MEDIAN=min(large)')
        text(100, 280, str(large[0][0]))
    else:
        text(25, 240, 'MEDIAN=(min(large)+max(small))/2')
        text(100, 280, '('+str(large[0][0])+'+'+str((-small[0][0]))+')/2='+str((large[0][0]-small[0][0])/2.0))
    text(25, 325, 'RESULTS')
    result_print(ans, 320)