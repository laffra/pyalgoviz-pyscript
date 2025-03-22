"""
 Big-O Notation 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Big-O Notation"
__author = "chris@chrislaffra.com"

def __algorithm():
    import math

    def computeBigO(functions, elements):
        operations = [[] for fn in functions]
        for e in elements:
            for n,fn in enumerate(functions):
                operations[n].append(fn(e))
        return operations

    def O_log_n(n): return math.log(n)
    def O_n(n): return n
    def O_n_log_n(n): return n * math.log(n)
    def O_n_2(n): return n * n
    def O_2_n(n): return 2 ** n
    def O_n_factorial(n): return math.factorial(n)

    functions = [ 
        O_log_n, O_n, O_n_log_n, O_n_2, O_2_n, O_n_factorial
    ]
    scores = computeBigO(functions, range(1, 51))
    for n,fn in enumerate(functions):
        print('%s    :    %s' % (fn, int(scores[n][-1])))

def __visualization():
    line(50, 50, 50, 400)
    line(50, 400, 480, 400)

    colors = ['darkgreen','blue','orange','red','purple','black']
    o1 = operations[0]
    rect(305, 75, 290, 195, 'lightyellow')
    text(320, 100, "n", 17)
    text(430, 100, len(o1), 17)

    for n,fn in enumerate(functions):
        x1,y1 = 50,400
        label = fn.__name__
        for k,value in enumerate(operations[n]):
            if y1>50:
                x2 = 50 + k*9
                y2 = 400 - value/2
                line(x1, y1, x2, y2, colors[n], 3)
                x1,y1 = x2,y2
        text(320, 125 + n*25, label, 17, color=colors[n])
        text(430, 125 + n*25, round(value,2), 17)
        text(x1-31, max(56 + n*15, y1-8), label, 16, color='white')
        text(x1-30, max(55 + n*15, y1-7), label, 15)

    rect(0, 0, 600, 50, 'white', 'white')
    text(250, 300, 'P', 25)
    text(130, 190, 'NP', 25)