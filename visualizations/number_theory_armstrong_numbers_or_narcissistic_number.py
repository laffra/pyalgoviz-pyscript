"""
 Number Theory - Armstrong Numbers or Narcissistic_number 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Number Theory - Armstrong Numbers or Narcissistic_number"
__author = "kalyan359"

def __algorithm():
    #Armstrong number http://en.wikipedia.org/wiki/Narcissistic_number
    #http://everything2.net/index.pl?node_id=1407017&displaytype=printable&lastnode_id=1407017

    def armstrong_number_checker(number):
        x = number
        pow = len(list(map(int,str(x))))
        return number == sum(map(lambda x: x**pow,map(int,str(x))))
   

    number_list = [1,152,153,370,371,383, 407, 1010,4150,9474]
    for number in number_list:
        print('%10s: %s' % (repr(number), armstrong_number_checker(number)))

def __visualization():
    #Title
    rect(180, 22, 300, 40, '#333')
    text(190, 52, 'Armstrong Numbers', 30, color='lightblue')

    def show(s, y, color,sign):
        rect(150, y, 55, 55)
        text(160, y+35, s, 15, 'Arial', color)
        if sign:
            # Two parllel lines see y positions are same
            line(220, 120, 240, 120, 'black', 5)
            line(220, 130, 240, 130, 'black', 5)
        else:
            # != sign
            line(220, 120, 240, 120, 'black', 5)
            line(220, 130, 240, 130, 'black', 5)
            line(220, 135, 240, 115, 'red', 5)
        for n,c in enumerate(map(int,str(s))):
            rect(250+n*90, y, 65, 55)
            text(260+n*90, y+35, str(c)+('*'+str(c))*(pow-1), 15, 'Arial', color)
            if n!=pow-1: # To handle the last '+' sign
                line(315+n*92, 125, 335+n*92, 125, 'black', 5)
                line(325+n*92, 135, 325+n*92, 115, 'black', 5)

    if armstrong_number_checker(number):
        color = 'teal'
        sign = True
        line(240, 300, 250, 325, color, 5)
        line(250, 325, 290, 275, color, 5)
    else:
        color = 'orange'
        sign = False
        line(240, 275, 290, 325, color, 5)
        line(240, 325, 290, 275, color, 5)

    
    show(number, 100, color,sign)