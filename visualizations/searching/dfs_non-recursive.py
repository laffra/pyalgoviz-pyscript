"""
 Searching - DFS - Non-Recursive 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Searching - DFS - Non-Recursive"
__author = "chris@chrislaffra.com"

def __algorithm():
    tree = (((None,5,(None,9,None)),10,((None,23,None),37,(None,44,None))),52,((None,56,None),68,(((None,79,None),87,None),89,((None,91,None),93,(None,94,None)))))

    def DFS(x, n):
        stack = [x]
        while stack:
            left, v, right = stack.pop()
            if v == n: 
                return v
            stack.extend(filter(None, [left, right]))

    for n in [9, 91, 44, 56, 79, 23, 94, -1]:
        print(n, DFS(tree, n))

def __visualization():
    def showTree(tx, ty, px, py, w, node):
        if not node: return
        color = 'orange' if node[1]==v else 'red' if node[1]==n else 'teal'
        if px: line(px, py-5, tx, ty-5, '#AAA', 3)
        l, value, r = node
        showTree(tx-w/2-10, ty+49, tx, ty, w/2, l)
        showTree(tx+w/2+10, ty+49, tx, ty, w/2, r)
        circle(tx, ty-5, 20, color)
        text(tx-9, ty, value, 16, 'Arial', 'white')

    showTree(260, 50, 0, 0, 250, tree)

    text(30, 330, 'Depth First Search Non-Recursive', 30, color='navy')
    text(30, 370, 'Search for %d' % n, 30, color='navy')

    beep(v*10, 100)