"""
 Sorting - NegPos Sort 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Sorting - NegPos Sort"
__author = "chris@chrislaffra.com"

def __algorithm():
    def negativePositiveSort(data):
        n = step = 0
        count = len(data)
        while step < count:
            if data[n] > 0:
                data.append(data.pop(n))
            else:
                n += 1
            step += 1
        
    original = [ -1, 1, 3, -2, -5, 5, 2 ]
    data = original[:]
    negativePositiveSort(data)

    print(original, '==>', data)

    # Given a sequence with n positive and negative numbers.
    # Sort it so that the negative numbers are in the front,
    # and the positive numbers are in the back.
    #
    # Preserve the original relative order of the numbers.
    #
    # o(n) time complexity and o(1) space complexity is perfect.

def __visualization():
    def chart(label, seq, y, highlight=False):
        text(40, y+4, label)
        line(90, y, 590, y, 'gray')
        for i,v in enumerate(seq):
            if highlight and n == i and step<count:
                color = 'red' 
            elif v<0:
                color = '#EEE'
            else:
                color = 'teal'
            rect(150 + i*50, y - max(0,15*v), 40, abs(15*v), color)
            text(160 + i*50, y - 15*v + 5 - 15*(1 if v>0 else -1), v, size=15)
        
    chart('Before:', original, 100)
    chart('After:', data, 335, True)