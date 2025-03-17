"""
 List Move 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "List Move"
__author = "laffra"

def __algorithm():
    def lstmov(data, src, dst, count):
        # safely move 'count' items in 'data' from 'src' to 'dst'
        # type(list, int, int, int) -> None
        if dst > src and dst <= src + count - 1:
            for n in range(count - 1, -1, -1):
                data[dst + n] = data[src + n]
        else:
            for n in range(count):
                data[dst + n] = data[src + n]
    
    def test(lst, src, dst, size, expected, case):
        lstmov(lst, src, dst, size)
        assert lst == expected, 'failed: %s' % case

    L = list(range(10))

    test(L[:], 1, 6, 3, [0,1,2,3,4,5,1,2,3,9], 'disjoint left')
    test(L[:], 6, 1, 3, [0,6,7,8,4,5,6,7,8,9], 'disjoint right')
    test(L[:], 1, 5, 5, [0,1,2,3,4,1,2,3,4,5], 'overlap left')
    test(L[:], 5, 1, 5, [0,5,6,7,8,9,6,7,8,9], 'overlap right')
    test(L[:], 3, 3, 5, [0,1,2,3,4,5,6,7,8,9], 'overlap full')
    test(L[:], 1, 6, 0, [0,1,2,3,4,5,6,7,8,9], 'noop')

def __visualization():
    rect(75, 40, 450, 35, 'black')
    text(130, 65, 'List move for case: ' + case, 24, 'Arial', 'white')

    w = 550 / len(data)

    def format_data(label, values, y, color_src, color_dst):
        text(25, y, label + ':')
        for i in range(len(data)):
            x = 25 + i * w
            color = 'white'
            if __lineno__ in [5,8]:
                if i == dst+n: color = color_dst
                if i == src+n: color = color_src
            rect(x, y + 10, w-10, w-10, color)
            text(x+15, y + 37, values[i], 21)

    def format_src_dst(label, n, y0, y1, y2):
        x1 = 45 + n * w
        x2 = max(x1, x1 + (count - 1) * w)
        text(x1 + size/2 * w, y0, label)
        line(x1, y1, x2, y1)
        line(x1, y1, x1, y2)
        line(x2, y1, x2, y2)

    format_src_dst('src', src, 120, 130, 150)
    format_src_dst('dst', dst, 250, 235, 215)
    format_data('data', lst, 150, 'lightgreen', 'pink')
    format_data('expected', expected, 300, 'white', 'white')