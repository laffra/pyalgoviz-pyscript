"""
 Trees - Prefix/Radix/Trie 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Trees - Prefix/Radix/Trie"
__author = "chris@chrislaffra.com"

def __algorithm():
    from collections import defaultdict

    prefixTree = lambda: defaultdict(prefixTree)

    def insert(x, k, v):
        if k: insert(x[k[0]], k[1:], v)
        else: x[''] = v

    def find(x, k):
        if k[:1] in x:
            return find(x[k[:1]], k[1:]) if k else x[k]
      
    data = [ 'tuple', 'in', 'test', 'tuples', 'type', 'tux', 'int' ]

    tree = prefixTree()

    for word in data:
        insert(tree, word, word.upper())
    
    print(find(tree, 'tuple'))
    print(find(tree, 'missing'))
    print(find(tree, 'test'))

def __visualization():
    def showTree(x, y, px, py, node, key=None):
        if px: 
            line(px, py+9, px, y+5, '#AAA', 3)
            line(px, y+5, x, y+5, '#AAA', 3)
        if key:
            rect(x-5, y-10, 35, 35)
            text(x+5, y+15, str(key), 25)
            py = y
        h = 0
        if isinstance(node, str):
            text(x+10, y+10, repr(node), 20, 'Courier', 'blue')
            h = 40
        else:
            for n in sorted(node.keys()):
                h += showTree(x+60, y+h, x+30, py, node[n], n)
        return h

    rect(10, 22, 310, 40, '#333')
    text(20, 52, 'Prefix/Radix/Trie Tree', 30, color='lightblue')
    showTree(20, 100, 0, 55, tree)

    for n,c in enumerate(word):
        rect(412+30*n, 28, 25, 25, 'lightyellow')
        text(420+30*n, 47, c, 18)
    text(350, 47, 'Add:', 18)
    beep(ord(k[0])*5, 100)