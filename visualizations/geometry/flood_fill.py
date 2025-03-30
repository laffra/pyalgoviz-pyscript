"""
 flood fill 
"""

#pylint: disable=missing-function-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=consider-using-f-string
#pylint: disable=undefined-variable
#pylint: disable=unused-import
#pylint: disable=invalid-name

__name = "flood fill"
__author = "KingRobertKing"

def __algorithm():
    grid = '''......#..#..
    ..#...#####.
    ..#.........
    ......#####.
    ..##.#.#....
    .#.#..#####.'''

    grid = [list(row) for row in grid.splitlines()]

    def flood(grid, i, j):
        inside_grid = 0 <= i < len(grid)
        inside_grid &= 0 <= j < len(grid[0])
        if inside_grid:
            can_be_filled = grid[i][j] == "."
            if can_be_filled:
                grid[i][j] = "*"
                flood(grid, i + 1, j)
                flood(grid, i - 1, j)
                flood(grid, i, j - 1)
                flood(grid, i, j + 1)

    print(grid)
    flood(grid, 0, 0)

def __visualization():
    progress = 1

    for i, row in enumerate(grid):
        for j, room in enumerate(row):
            fill = {'*': 'pink', '.': 'white', '#': 'black'}[room]
            if fill == "pink": progress += 1
            rect(40*j + 5, 40*i + 5, 40, 40, fill=fill, border='black')
            text(40*j + 20, 40*i + 28, room, size=15, font='Arial', color='black')

    if __lineno__ == 16: beep(300 + progress * 50, 200)
    if __lineno__ == 15 and not can_be_filled: beep(300, 200)

    text(20, 320, "FLOOD FILL", size=90)