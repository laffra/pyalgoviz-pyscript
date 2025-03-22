"""
 Dynamic Programming - Knapsack 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Dynamic Programming - Knapsack"
__author = "chris@chrislaffra.com"

def __algorithm():
    def knapsack(items, maxweight):
        best = {}
    
        def B(n, W):
            b = 0 if n == 0 else best.get((n,W)) 
            if b is None:
                v, w = items[n-1]
                b = B(n-1,W) if w>W else max(B(n-1,W), B(n-1,W-w)+v)
            best[(n,W)] = b
            return b

        W = maxweight
        result = []
        for n in range(len(items), 0, -1):
            if B(n, W) != B(n - 1, W):
                result.append(items[n - 1])
                W -= items[n - 1][1]
        return result

    items = [(4, 1), (6, 4), (1, 1), (2, 1)]
    import random
    random.shuffle(items)

    print(knapsack(items, 6))

    # Derived from:  http://codereview.stackexchange.com/a/20581

def __visualization():
    text(35, 90, 'Dynamic Programming: Knapsack', 35)

    chosen = map(items.index, result)

    pink = []
    w = maxweight
    for i in range(len(items), 0, -1):
        if best.get((i, w)) != best.get((i - 1, w)):
            pink.append((i,w))
            w -= items[i-1][1]
            
    def showBest(X, Y):
        for y in range(maxweight):
            text(X-15, Y+42+y*25, y, 15, 'Arial', '#CCC')
        for x in range(len(items)):
            text(X+5+x*30, Y+13, x, 15, 'Arial', '#CCC')
            for y in range(maxweight):
                v = best.get((x,y))
                v = '' if v is None else v
                color = 'orange' if x==n and y==W else '#f5f5f5'
                if not v is '': color = 'white'
                if (x,y) in pink: color='pink'
                rect(X+x*30, Y+25+y*25, 25, 20, color)
                text(X+5+x*30, Y+40+y*25, v, size=15)
            text(X+45, Y+40+(y+1)*25, 'best', 12, 'Arial', '#CCC')
    
    def showKnapsack(X, Y, label, seq):
        text(X, Y, label, 20)
        y = Y+10
        for value,weight in seq:
            rect(X, y, 25, 20)
            text(X+5, y+16, value, size=15)
            rect(X+35, y, 25, 20)
            text(X+40, y+16, weight, size=15)
            if seq == result:
                y2 = Y+25*(items.index((value,weight))+1)-2
                line(X, y+12, 340, y2, '#CCC')
            y += 25
        text(X-30, y+20, 'value', 12, color='#DDD')
        text(X+65, y+20, 'weight', 12, color='#DDD')
        line(X, y, X+65, y, '#CCC')
        text(X+5, y+20, sum(v for v,w in seq), size=15)
        text(X+40, y+20, sum(w for v,w in seq), size=15)
        
    showBest(75, 160)
    showKnapsack(280, 195, 'Input:', items)
    showKnapsack(430, 195, 'Result:', result)

    text(430, 390, 'Max: %d' % maxweight, 25)