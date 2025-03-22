"""
 Graphs - MST 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Graphs - MST"
__author = "chris@chrislaffra.com"

def __algorithm():
    import heapq

    def primsMinimumSpanningTree(graph):
        queue = [(0, '#', list(graph.keys())[0])]
        tree = []
        seen = set()
        while queue:
            _, v0, v1 = heapq.heappop(queue)
            seen.add(v0)
            if v1 not in seen:
                tree.append((v0,v1))
                for (v2, c) in graph[v1].items():
                    heapq.heappush(queue, (c, v1, v2))
        return tree
            
    graph = {
        'a': {'w': 14, 'x': 7, 'y': 9},
        'b': {'w': 9, 'z': 6},
        'w': {'a': 14, 'b': 9, 'y': 2},
        'x': {'a': 7, 'y': 10, 'z': 15},
        'y': {'a': 9, 'w': 2, 'x': 10, 'z': 11},
        'z': {'b': 6, 'x': 15, 'y': 11},
    } 
    print(primsMinimumSpanningTree(graph))

    # See http://en.wikipedia.org/wiki/Prim's_algorithm

def __visualization():
    rect(10, 22, 530, 40, '#333')
    text(20, 52, "Prim's Minimum Spanning Tree", 30, color='lightblue')

    pos = {
       '#' : (0,100),
       'a':(50,100), 'x':(140,0), 'y':(160,200),
       'w':(350,0), 'z':(330,200), 'b':(450,100)
    }

    for v in graph.keys():
        x1, y1 = pos[v]
        for other,w in graph[v].items():
            x2, y2 = pos[other]
            line(80+x1, 150+y1, 80+x2, 150+y2, '#ccc')
            text(80 + x1+(x2-x1)/4, 150 + y1+(y2-y1)/4-10, w, 15)

    for v,other in tree:
        x1, y1 = pos[v]
        x2, y2 = pos[other]
        line(80+x1, 150+y1, 80+x2, 150+y2, 'red', 5)
        
    for value, location in pos.items():
        x, y = location
        color = 'orange' if value in seen else 'lightyellow'
        circle(80+x, 150+y, 15, color)
        text(77+x, 155+y, value, 15)