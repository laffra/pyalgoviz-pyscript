"""
 Graphs - Dijkstra Shortest Path 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Graphs - Dijkstra Shortest Path"
__author = "chris@chrislaffra.com"

def __algorithm():
    import heapq

    def shortestPath(graph, start, end):
        queue,seen = [(0, start, [])], set()
        while True:
            (cost, v, path) = heapq.heappop(queue)
            if v not in seen:
                path = path + [v]
                seen.add(v)
                if v == end:
                    return cost, path
                for (next, c) in graph[v].items():
                    heapq.heappush(queue, (cost + c, next, path))
            
    graph = { 
       'a': {'w': 14, 'x': 7, 'y': 9}, 
       'b': {'w': 9, 'z': 6}, 
       'w': {'a': 14, 'b': 9, 'y': 2}, 
       'x': {'a': 7, 'y': 10, 'z': 15}, 
       'y': {'a': 9, 'w': 2, 'x': 10, 'z': 11}, 
       'z': {'b': 6, 'x': 15, 'y': 11}, 
    }
    cost, path = shortestPath(graph, 'a', 'b')
    print(cost, path)
    # Based on http://code.activestate.com/recipes/119466

def __visualization():
    rect(10, 22, 320, 40, '#333')
    text(20, 52, 'Dijkstra Shortest Path', 30, color='lightblue')

    visited = seen

    pos = {
       'a':(0,100), 'x':(150,0), 'y':(150,200),
       'w':(300,0), 'z':(300,200), 'b':(450,100)
    }

    for v, location in pos.items():
        x1, y1 = location
        for other,w in graph[v].items():
            x2, y2 = pos[other]
            line(80+x1, 150+y1, 80+x2, 150+y2, '#ccc')
            text(80 + x1+(x2-x1)*1/3-10, 150 + y1+(y2-y1)*1/3, w, 15)
        
    for value, location in pos.items():
        x, y = location
        color = 'orange' if value in visited else 'lightyellow'
        color = 'pink' if value in path else color
        circle(80+x, 150+y, 30, color)
        text(72+x, 160+y, value, 35)