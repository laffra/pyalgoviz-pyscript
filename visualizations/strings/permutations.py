"""
 Strings - Permutations 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Strings - Permutations"
__author = "chris@chrislaffra.com"

def __algorithm():
    def permutations(s):
        if len(s) <= 1: 
            yield s
        else:
            for i in range(len(s)):
                for p in permutations(s[:i] + s[i+1:]):
                    yield s[i] + p
        
    input = 'ABCD'

    for permutation in enumerate(permutations(input)):
        print(repr(permutation[1]),)
    print

def __visualization():
    number, perm = permutation

    text(35, 70, 'Input:', 21)
    for n,c in enumerate(input):
        color = 'orange' if c == perm[0] else 'lightyellow'
        rect(250 + n*30, 50, 25, 25, color)
        text(255 + n*30, 70, c, 21)
    
    text(35, 170, 'Permutation %d:' % (number+1), 21)
    for n,c in enumerate(perm):
        rect(250 + n*30, 150, 25, 25, 'lavender')
        text(255 + n*30, 170, c, 21)
        line(262 + n*30, 150, 262 + input.index(c)*30, 75, '#AAA')
    
    rect(35, 272, 290, 40, '#333')
    text(45, 302, 'String Permutations', 30, color='lightblue')