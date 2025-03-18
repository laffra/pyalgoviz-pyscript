"""
 Strings - Anagram Check 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Strings - Anagram Check"
__author = "laffra"

def __algorithm():
    from collections import defaultdict, Counter

    def anagram(s1, s2):
        counts = defaultdict(int)
        for c in s1:
            counts[c] += 1

        for c in s2:
            counts[c] -= 1

        return not any(counts.values())

        # this works as well, using 2N temporary space:
        return Counter(s1) == Counter(s2)

        
    strings = [
       ('secure', 'rescue'),
       ('conifers', 'fircone'),
       ('google', 'facebook'),
    ]
    for s1,s2 in strings:
        print('%10s %10s: %s' % (repr(s1), repr(s2), anagram(s1, s2)))


    #
    # Given a string, check if it is a anagram.  
    #

def __visualization():
    def show(s, y, label, color):
        text(30, y+20, label, 20, 'Arial', 'teal')
        for n,c in enumerate(s):
            rect(150+n*30, y, 25, 25, color(c))
            text(155+n*30, y+20, c, 20, 'Arial', 'white')

    show(s1, 100, 'first:', lambda c: 'orange' if counts[c]>0 else 'teal')
    show(s2, 200, 'second:', lambda c: 'red' if counts[c] else 'teal')