"""
 Boyer-Moore-Horspool 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Boyer-Moore-Horspool"
__author = "namnguyen@google.com"

def __algorithm():
    # Boyer-Moore-Horspool algorithm with visualization.
    # Copyright 2014 Nam T. Nguyen
    # Released under the APL version 2

    haystack = 'abaaabbababcabdacbaabababc'
    needle = 'cbaababa'

    def match(haystack, needle):
        len_needle = len(needle)
        len_haystack = len(haystack)
    
        if not len_needle:
            return True
        if len_needle > len_haystack:
            return False
    
        # set up
        skip_list = {}
        for idx, c in enumerate(needle[ : -1]):
            skip_list[c] = (len_needle - 1) - idx
    
        # reverse match
        pos = len_needle - 1
        while pos < len_haystack:
            for i in range(len_needle):
                h_index = pos - i
                n_index = -(i + 1)
                if haystack[h_index] != needle[n_index]:
                    skip = skip_list.get(haystack[pos], len_needle)
                    pos += skip
                    break
            else:
                return True
    
        return False

    assert match(haystack, needle)

def __visualization():
    box_width = 20
    box_height = 20

    def box_text(x, y, c, color):
        rect(x, y, box_width, box_height, fill=color)
        text(x + 6, y + 14, c)

    text(50, 55, "TEXT")
    color = 'white'
    for i, c in enumerate(haystack):
        box_text(i * box_width + 50, 60, c, color)

    start = pos - len_needle + 1
    text(start * box_width + 50, 95, 'PATTERN')
    for i in range(len_needle):
        j = i + start
        box_text(j * box_width + 50, 100, needle[i], 'white')

    if 25 <= __lineno__ <= 31:
        if __lineno__ >= 28:
            if haystack[h_index] != needle[n_index]:
                color = 'red'
            else:
                color = 'green'
        box_text(h_index * box_width + 50, 60, haystack[h_index], color)