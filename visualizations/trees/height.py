"""
 Trees - Height 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Trees - Height"
__author = "chris@chrislaffra.com"

def __algorithm():
    L,V,R = 0,1,2

    def insert(root, node):
        d = L if root[V] > node[V] else R
        root[d] = node if not root[d] else insert(root[d], node)
        return root
    
    def createTree(data):
        tree = [None, data[0], None]
        for v in data[1:]:
            insert(tree, [None, v, None])
        return tree

    def height(t):
        if t:
            d1,p1 = height(t[L])
            d2,p2 = height(t[R])
            return (max(d1+1,d2+1), (p1 if d1>d2 else p2) + t[1:2])
        return (0,[])

    from random import sample
    data = sample(range(0, 100), 20)
    tree = createTree(data)
    height,path = height(tree)

    print('height =', height)
    print('longest path =', path)

def __visualization():
    beep(v*30, 100)

    def showTree(x, y, px, py, w, treeNode):
        if treeNode:
            l, v, r = treeNode
            try:
                color = 'orange' if treeNode==t else 'red'                                 if v in path else 'teal'
            except:
                color = 'teal'
            if px:
                line(px, py-5, x, y-5, '#AAA', 3)
            showTree(x-w/2-10, y+39, x, y, w/2, l)
            showTree(x+w/2+10, y+39, x, y, w/2, r)
            circle(x, y-5, 15, color)
            text(x-5, y, v, 13, 'Arial', 'white')

    showTree(300, 50, 0, 0, 230, tree)

    text(50, 400, f'Height is {height}', 20, 'Arial', 'navy')