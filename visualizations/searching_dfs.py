"""
 Searching - DFS 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Searching - DFS"
__author = "laffra"

def __algorithm():
    tree = (((None,5,(None,9,None)),10,((None,23,None),37,(None,44,None))),52,((None,56,None),68,(((None,79,None),87,None),89,((None,91,None),93,(None,94,None)))))

    def DFS(x, n):
        if x:
            left, v, right = x
            return v if v == n else DFS(left, n) or DFS(right, n)

    for n in [9, 91, 44, 56, 79, 23, 94, -1]:
        print(n, DFS(tree, n))

def __visualization():
    def showTree(tx, ty, px, py, w, node, depth):
        if not node: return
        color = 'orange' if node==x else 'red' if node[1]==n else 'teal'
        if px: line(px, py-5, tx, ty-5, '#AAA', 3)
        l, v, r = node
        showTree(tx-w/2-10, ty+49, tx, ty, w/2, l, depth+1)
        showTree(tx+w/2+10, ty+49, tx, ty, w/2, r, depth+1)
        circle(tx, ty-5, 20, color)
        text(tx-9, ty, v, 16, 'Arial', 'white')
        if color == "orange":
            beep(500+depth*200, 100)

    showTree(260, 50, 0, 0, 250, tree, 1)

    text(30, 330, 'DFS - Depth First Search', 30, color='navy')
    text(30, 370, 'Search for %d' % n, 30, color='navy')