"""
 Searching - Linear Search 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Searching - Linear Search"
__author = "chris@chrislaffra.com"

def __algorithm():
    def linearSearch(seq, t):
        for n,v in enumerate(seq):
            if v == t:
                return n
        # we scanned the whole sequence, and did not find t
        return -1

    data = list(range(30))
  
    for t in [0, 29, -1, 8, 23, 14]:
        checksum = data.index(t) if t in data else -1
        print('linear search for', t, '==>',)
        print(linearSearch(data, t), checksum)

def __visualization():
    barchart(10, 10, 500, 150, data, highlight=n, scale=3)

    text(10, 300, 'running linear search for %d' % t)
    text(10, 330, 'data.index(%d) = %d' % (t, checksum))

    if v==checksum:
        msg,color = 'FOUND %d at %d' % (v,n),'teal'
    else:
        msg,color = 'compare with %d' % v, 'orange'
    
    x = 35 + n*460/len(data)
    line(x, 200, x, 175, color, 3)
    text(x-9, 223, msg, 18, color=color)

    beep(n * 100, 50)