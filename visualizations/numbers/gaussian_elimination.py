"""
 Gaussian Elimination 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "Gaussian Elimination"
__author = "KingRobertKing"

def __algorithm():
    '''
    A*x = b

    e.g.

    2x + y - z = 8,
    -3x -y +2x = -11
    -2x + y + 2z = -3

    see http://en.wikipedia.org/wiki/Gaussian_elimination
    '''

    __author__ = "www.google.com/+robertking"

    A = [
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2]
    ]

    b = [8, -11, -3]



    def reduce(A, b, i):
        if i == len(A):
            return
        if A[i][i] == 0:
            #swap as need non zero pivot
            for j in range(i + 1, len(A)):
                if A[j][i] != 0:
                    A[i], A[j] = A[j], A[i]
                    break
        if A[i][i] == 0:
            #no pivots
            reduce(A, b, i + 1)

        pivot = float(A[i][i])
        A[i] = [v/pivot for v in A[i]]
        b[i] = b[i]/pivot

        for j in range(i + 1, len(A)):
            to_zero = A[j][i]
            A[j] = [v_row - to_zero * v_pivot for v_row, v_pivot in zip(A[j], A[i])]
            b[j] = b[j] - to_zero * b[i]

        reduce(A, b, i + 1)

    reduce(A, b, 0)

    print(A)
    print(b)

def __visualization():
    s = 100
    indent = 50

    def draw_system(pivot):
        for i, row in enumerate(A):
            bi = b[i]
            rect(3 * s + s, indent + s*i, s, s, fill='white', border='blue')
            text(3 * s + s + s/2 - 10, indent + s * i + s/2 + 10, bi, size=23, font='Arial', color='black')
            text(3 * s + s - s/3, indent + s * i + s/2 + 10, "=", size=23, font='Arial', color='black')
            for j, v in enumerate(row):
                fill = 'white'
                if i <= pivot and j >= i:
                    fill = 'pink'
                    if i == j:
                        fill = 'yellow'
                rect(indent + s*j, indent + s * i, s, s, fill=fill, border='black')
                txt = str(v) + " " + "XYZ"[j]
                text(indent + s*j + s/2 - 26, indent + s * i + s/2 + 10, txt, size=23, font='Arial', color='black')
       
    #diag = indent + s * (i + 0.5)
    pivot = i
    draw_system(pivot)            



    if pivot >= 2:
        rect(260, 265, 220, 66, fill='transparent', border='red')
        text(20, 410, "Z = -1 so we can now find Y = 3 etc", size=32)
    else:
        text(20, 410, "Gaussian Elimination", size=32)