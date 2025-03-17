"""
 calc_autocorrelation_optimized 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "calc_autocorrelation_optimized"
__author = "WangYe.Hope"

def __algorithm():
    x = [6,3,1,4,2,6,3,1,1,2,1,5]
    x = [float(xx) for xx in x]
    n = len(x)
    R = [0] * n # 只用一个buffer
    s = 0  # 用于计算平均值
    i = 0
    for i in range(n):
        for k in range(n):
            if k <= i:
                R[k] += x[i - k] * x[i]
            if k + i < n:
                R[k] -= x[i] ** 2 / n
                if i > 0:
                    R[k] -= 2 * x[i] * s / n
            if k - i >= 1:
                R[k] += x[i] ** 2 / n
                if i > 0:
                    R[k] += 2 * x[i] * s / n
        sum_k = 0
        for k in range(n):
            if 0 < k <= i:
                R[k] += x[i] * sum_k / n
            elif k > i:
                break
            sum_k += x[k]
        sum_k = 0
        for k in range(n)[::-1]:
            if n - k - 1 < i:
                sum_k += x[n - 1 - k]
                R[k] -= x[i] * sum_k / n
        s += x[i]
    s /= n
    for k in range(n):
        R[k] -= k * s ** 2

def __visualization():
    box_width = 40
    box_height = 20

    def box_text(x, y, c, color):
        rect(x, y, box_width, box_height, fill=color)
        text(x + 6, y + 14, float(int(c*100))/100)

    def array_print(dataset, location, color_func=lambda x: 'white'):
        for i, c in enumerate(dataset):
            box_text(i * box_width + 85, location + 10, 
                     c, color_func(i))


    text(50, 90, "SAMPLES")
    array_print(x, 85, lambda x: 'white' if x != i else 'red')
    text(50, 135, 'BUFFER')
    array_print(R, 130, lambda x: 'white')