"""
 Sorting - Using Custom Keys 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Sorting - Using Custom Keys"
__author = "laffra"

def __algorithm():
    cities = ['Madrid', 'lima', 'Amsterdam', 'Berlin']

    def sort(data, fn):
        return sorted(data, key=fn)  
    
    custom = [
        len,            # sort by number of chars in name
        str.lower,        # sort names in lowercase order
        lambda x: x,    # use the city name to sort (i.e., a no-op)
    ]

    for k in custom:
        result,key = sort(cities, k), k

def __visualization():
    def show(values, y, label, arrow=0):
        text(10, y+20, label, 15)
        for n,v in enumerate(values):
            x = 120+n*110
            rect(x, y, 100, 25, 'lightyellow')
            indent = max(0, (100 - len(str(v))*9)//2)
            text(x+5+indent, y+18, v, 15)
            if arrow:
                x = 285 if arrow==1 else x
                line(x+50, y+35, x+50, y+85, '#AAA')
                line(x+40, y+65, x+50, y+85, '#AAA')
                line(x+60, y+65, x+50, y+85, '#AAA')

    text(120, 68, '%d of %d =' % ((1+custom.index(key)),len(custom)), 18)
    text(190, 68, str(key), 18)
    text(10, 68, 'Sort key:', 15)

    show(cities, 150, 'Cities:', 4)
    show(map(key, cities), 250, 'Proxy Values:', 1)
    show(result, 350, 'Sorted Result:')