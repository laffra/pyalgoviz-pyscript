"""
 ThreeSum - 1 - Brute Force 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "ThreeSum - 1 - Brute Force"
__author = "laffra"

def __algorithm():
    import itertools

    def threesum(L):
        # this is O(n^3) in both space and time
        triples = itertools.combinations(L, 3)
        unique = set([tuple(sorted(t)) for t in triples if sum(t) == 0])
        return map(list, unique)

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
    if __lineno__ == 15:
        for n, (input, output) in enumerate(tests):
            text(10,  20 + n * 50, '%d' % n, 15)
            text(50,  20 + n * 50, 'Input:', 15)
            text(120, 20 + n * 50, input, 15)
            text(50,  20 + n * 50 + 20, 'Output:', 15)
            text(120, 20 + n * 50 + 20, output, 15)