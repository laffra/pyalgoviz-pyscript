"""
 Strings - Prefix/Spell Tree 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Strings - Prefix/Spell Tree"
__author = "laffra@google.com"

def __algorithm():
    from collections import defaultdict

    prefixTree = lambda: defaultdict(prefixTree)

    def insert(x, k, v, cost):
        if k: 
            insert(x[k[0]], k[1:], v, cost)
            if len(k)>1:
                insert(x[k[1]], k[2:], v, cost+COST_SKIP)
                insert(x[k[1]], k[0]+k[2:], v, cost+COST_SWAP)
                if len(k)>2:
                    insert(x[k[2]], k[:2]+k[3:], v, cost+COST_SWAP2)
        else: 
            entry = (cost, v)
            x[''] = x[''] + [entry] if '' in x else [entry]

    def find(prefix, k, penalty=0):
        if k:
            if k[:1] in prefix:
                return find(prefix[k[:1]], k[1:], penalty) 
            for c in prefix:
                if c:
                    return find(prefix[c], k[1:], penalty+COST_SUBST) 
        else:
            return [(cost+penalty, value) for cost,value in prefix[k]]
        return [(-1,'')]
      
    COST_SKIP  = 1     # cost of  "cart" ==> "cat"
    COST_SWAP  = 2     # cost of  "cta"  ==> "cat"
    COST_SWAP2 = 4   # cost of  "tac"  ==> "cat"
    COST_SUBST = 3   # cost of  "cit"  ==> "cat"

    dictionary = [ 'cat', 'act' ]
    tree = prefixTree()
    for d in dictionary:
        insert(tree, d, d, 0)
    
    words = ['cat','tac','dat','cta','act','ace','ice','ict','tic']
    for word in words:
        threshold = len(word) * 1.5
        result = sorted(find(tree, word))
        matches = list(filter(lambda x: x[0]<=threshold, result))
        match = matches[0] if matches else (-1,'')
        print('%3s ==> %3s : %s ==> %s' % (word,match[1],result,matches))

def __visualization():
    def showTree(x, y, px, py, node, key=None):
        if px: 
            line(px, py+15, px, y+5, '#AAA', 3)
            line(px, y+5, x, y+5, '#AAA', 3)
        h = 0
        if key:
            py = y
        if isinstance(node, list):
            matches = ', '.join(['%s:%s' % (s,v) for s,v in sorted(node)])
            text(250, y+10, matches, 15, 'Courier', 'blue')
            line(x, y+5, 250, y+5, '#AAA', 3)
            h = 30
        else:
            for n in sorted(node.keys()):
                h += showTree(x+40, y+h, x+5, py, node[n], n)
        if key:
            rect(x-5, y-10, 25, 25, 'orange' if node==prefix else 'white')
            text(x+2, y+8, str(key).upper(), 18)
        return h

    rect(10, 22, 250, 40, '#333')
    text(20, 52, 'Prefix/Spell Tree', 30, color='lightblue')
    text(320, 52, 'Search: %s' % word, 30, color='teal')
    showTree(20, 100, 0, 55, tree)