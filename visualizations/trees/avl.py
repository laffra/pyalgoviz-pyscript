"""
 Trees - AVL 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Trees - AVL"
__author = "chris@chrislaffra.com"

def __algorithm():
    L,V,R,D = 0,1,2,3

    def depth(x): return x and x[D] or 0

    def insert(x, v):
        edge = L if x[V] > v else R
        x[edge] = insert(x[edge], v) if x[edge] else [None,v,None,1]
        rebalance(x)
        x[D] = 1 + max(depth(x[L]), depth(x[R]))
        return x

    def rebalance(x):
        ld,rd = depth(x[L]), depth(x[R])
        if abs(ld-rd) > 1:
            l,r = (L,R) if ld>rd else (R,L)
            c = x[l]
            x[V],x[l],x[r],c[l],c[r],c[V] = c[V],c[l],c,c[r],x[r],x[V]
            c[D] = 1 + max(depth(c[l]), depth(c[r]))
            x[D] = 1 + max(depth(x[l]), depth(x[r]))
    
    def avlTree(data):
        tree = [None, data[0], None, 1] # [left, value, right, depth]
        for newValue in data[1:]:
            insert(tree, newValue)
        return tree

    data = range(15,0,-1)
    tree = avlTree(data)        # create a balanced binary search tree

def __visualization():
    L,V,R,D = 0,1,2,3
        
    def showTree(tx, ty, px, py, w, node):
        if node:
            if px: line(px, py-5, tx, ty-5, '#AAA', 3)
            showTree(tx-w/2-10, ty+40, tx, ty, w/2, node[L])
            showTree(tx+w/2+10, ty+40, tx, ty, w/2, node[R])
            color = 'brown' if node[V]==newValue else 'orange' if node==x else 'teal'
            circle(tx-5, ty-9, 15, color)
            text(tx-15, ty-5, node[V], 17, 'Arial', 'white')
            beep(newValue*100, 10)

    rect(10, 22, 205, 40, '#333')
    text(20, 52, 'AVL Tree', 30, color='lightblue')
    showTree(300, 100, 0, 0, 250, tree)

    text(50, 400, 'Depth of each left and right branch differ by at most 1.', 20)

    text(250, 47, 'Adding: %d' % newValue, 18)