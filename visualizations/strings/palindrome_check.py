"""
 Strings - Palindrome Check 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Strings - Palindrome Check"
__author = "chris@chrislaffra.com"

def __algorithm():
    def palindrome(string):
        return string == string[::-1]
        
    strings = [
       'acdc',
       'kayak',
       'deadmau5',
       'abba',
    ]
    for s in strings:
        print('%10s: %s' % (repr(s), palindrome(s)))


    #
    # Given a string, check if it is a palindrome.  
    #

def __visualization():
    def show(s, y, color, label):
        text(30, y+20, label, 20, 'Arial', color)
        for n,c in enumerate(s):
            rect(150+n*30, y, 25, 25)
            text(155+n*30, y+20, c, 20, 'Arial', color)

    if s == s[::-1]:
        color = 'teal'
        line(40, 300, 50, 325, color, 5)
        line(50, 325, 90, 275, color, 5)
    else:
        color = 'red'
        line(40, 275, 90, 325, color, 5)
        line(40, 325, 90, 275, color, 5)

    show(s, 100, color, 'original:')
    show(s[::-1], 200, color, 'reversed:')

    beep(500+__lineno__*200, 1000)