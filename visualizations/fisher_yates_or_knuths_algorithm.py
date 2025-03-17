"""
 Fisher Yates or Knuths Algorithm 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Fisher Yates or Knuths Algorithm"
__author = "kalyan359"

def __algorithm():
    # I always wondered how do people come up with Song Shuffle algorithms? Here is a most simple yet unbaised shuffle algorithm for you all.
    # More on Knuths shuffle algorithm - http://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle

    import random

    unshuffled_list = list(range(8))
    shuffled_list = []
    for i in range(8):
        index = random.randrange(0,8-i)
        shuffled_list.append(unshuffled_list[index])
        unshuffled_list.remove(unshuffled_list[index])

def __visualization():
    X, Y, D = 50, 150, 40


    text(20, 130, 'Unshuffled list', 15)
    #unshuffled list:
    for x in unshuffled_list:    # iteration for 8 times
        color = 'pink' if x == index else 'orange'
        rect(X+x*D, Y+0*D, D-5, D-5, color)
        text(X+x*D+2, Y+0*D+D/2, x, 15)

    text(20, 270, 'Shuffled list Generation', 15)
    #shuffled list
    for y in range(8):
        rect(X+y*D, Y+4*D, D-5, D-5, 'teal')
        text(X+y*D+2, Y+4*D+D/2, shuffled_list[y], 15)

    
    rect(X, 42, 415, 40, '#333')
    text(X+15, 72, 'Fisher Yates or Knuth shuffle', 30, color='lightblue')