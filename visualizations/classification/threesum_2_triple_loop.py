"""
 ThreeSum - 2 - Triple Loop 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "ThreeSum - 2 - Triple Loop"
__author = "chris@chrislaffra.com"

def __algorithm():
    def threesum(L):
        result = set()
        for i in range(len(L) - 2):
            for j in range(i + 1, len(L) - 1):
                for k in range(j + 1, len(L)):  # O(n^3)
                    if L[i] + L[j] + L[k] == 0:
                        result.add(tuple(sorted((L[i], L[j], L[k]))))
            if L[i] == 0:
                break
        return map(list, result)

    tests = (
        ([0, 0, 0], [[0, 0, 0]]),
        ([-1,0,1,2,-1,-4], [[-1, -1, 2], [-1, 0, 1]]),
        ([-2,0,-2,1,0,4,0,-1] * 10,
         [[-1, 0, 1], [-2, -2, 4], [0, 0, 0], [-2, 1, 1]]),
    )
    for n, (input, output) in enumerate(tests):
        print(n, 'input', input)
        print(n, 'expected:', output)
        print(n, 'actual:', threesum(input))

def __visualization():
    if __lineno__ == 18:
        for n, (input, output) in enumerate(tests):
            text(10,  20 + n * 50, '%d' % n, 15)
            text(50,  20 + n * 50, 'Input:', 15)
            text(120, 20 + n * 50, input, 15)
            text(50,  20 + n * 50 + 20, 'Output:', 15)
            text(120, 20 + n * 50 + 20, output, 15)