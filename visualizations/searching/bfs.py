"""
 Searching - BFS 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Searching - BFS"
__author = "chris@chrislaffra.com"

def __algorithm():
    tree = (((None,6,(None,9,None)),10,((None,23,None),37,(None,44,None))),52,((None,56,None),68,(((None,79,None),87,None),89,((None,91,None),93,(None,94,None)))))

    def BFS(root, n):
        queue = [root]
        while queue:
            left, v, right = queue.pop(0)
            if v == n: 
                return v
            queue.extend(filter(None, [left, right]))

    for n in [9, 91, 44, 56, 79, 23, 94, -1]:
        print(n, BFS(tree, n))

def __visualization():
    def showTree(tx, ty, px, py, w, node, depth):
        if not node: return
        color = 'orange' if node in queue else 'red' if node[1]==n else 'teal'
        if px: line(px, py-5, tx, ty-5, '#AAA', 3)
        l, v, r = node
        showTree(tx-w/2-10, ty+49, tx, ty, w/2, l, depth+1)
        showTree(tx+w/2+10, ty+49, tx, ty, w/2, r, depth+1)
        circle(tx, ty-5, 20, color)
        text(tx-9, ty, v, 16, 'Arial', 'white')
        if color=="orange":
            beep(500+depth*200, 100)

    showTree(260, 50, 0, 0, 250, tree, 1)

    text(30, 330, 'BFS - Breath First Search', 30, color='navy')
    text(30, 370, 'Search for %d' % n, 30, color='navy')