"""
 calc_var_optimized 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "calc_var_optimized"
__author = "WangYe.Hope"

def __algorithm():
    nums = [1.2,2.3,1.5,6.3,2.4,5.0,3.5,1.6,2.3,5.6,2.6,3.4,2.4,4.3]
    n = len(nums)
    k = 7
    ret = []
    s = 0
    S = 0
    for ni in range(n):
        s += nums[ni]
        S += nums[ni]**2
        if ni >= k:
            s -= nums[ni-k]
            S -= nums[ni-k]**2
            ret.append(S/k-s**2/k**2)

def __visualization():
    box_width = 30
    box_height = 20

    def box_text(x, y, c, color):
        rect(x, y, box_width, box_height, fill=color)
        text(x + 6, y + 14, float(int(c*100))/100)

    def array_print(dataset, location, color_func=lambda x: 'white'):
        for i, c in enumerate(dataset):
            box_text(i * box_width + 85, location + 10, 
                     c, color_func(i))


    text(50, 90, "SAMPLES")

    array_print(nums, 85, lambda x: 'white' if x != ni else 'red')
    if ni >= k:
        text(50, 135, 's=s+nums[i]-nums[i-k]='+str(s))
        text(50, 160, 'S=S+nums[i]^2-nums[i-k]^2='+str(S))
    else:
        text(50, 135, 's=s+nums[i]='+str(s))
        text(50, 160, 'S=S+nums[i]^2='+str(S))
    #array_print(buffer, 130, lambda x: 'white' if x != nj else 'green')
    #text(150, 135, 'mean='+str(s))
    text(50, 180, 'RESULTS')
    array_print(ret, 175, lambda x: 'white')