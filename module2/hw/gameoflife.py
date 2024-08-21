# ********************************* Game of Life *********************************

import comp140_game_of_life as life

def update(grid, height, width):
    grid_act = []
    for i in range(height):
        grid_w = []
        for j in range(width):
            grid_w.append(-1)
        grid_act.append(grid_w)
    
    def count_live_neighbors(grid, i, j, height, width):
        live_neighbors = 0
        for x in range(max(0, i-1), min(height, i+2)):
            for y in range(max(0, j-1), min(width, j+2)):
                if (x != i or y != j) and grid[x][y] == 1:
                    live_neighbors += 1
        return live_neighbors
    
    for i in range(height):
        for j in range(width):
            live_neighbors = count_live_neighbors(grid, i, j, height, width)
            if grid[i][j] == 0:
                if live_neighbors == 3:
                    grid_act[i][j] = 5
                else:
                    grid_act[i][j] = -5
            else:
                if live_neighbors == 2 or live_neighbors == 3:
                    grid_act[i][j] = 5
                else:
                    grid_act[i][j] = -5
    
    for i in range(height):
        for j in range(width):
            if grid_act[i][j] == -5:
                grid[i][j] = 0
            elif grid_act[i][j] == 5:
                grid[i][j] = 1
    
    return grid

    """
    Update the grid according to the rules of the Game of Life.

    The grid is a list of lists.  The outer list should contain
    "height" lists, each of which has "width" elements.  Each element
    of the inner lists is either 1 (live) or 0 (dead).  This means you
    would index the grid as grid[row][col], where row is between 0 and
    height-1 and col is between 0 and width-1.
    """

"""    
# Test 1
grid1 = [[0, 1, 0],
         [0, 1, 0],
         [0, 1, 0]]
update(grid1, 3, 3)
print("Expected result:", [[0, 0, 0], [1, 1, 1], [0, 0, 0]])
print("Actual result:  ", grid1)

print("------")

update(grid1, 3, 3)
print("Expected result:", [[0, 1, 0], [0, 1, 0], [0, 1, 0]])
print("Actual result:  ", grid1)

print("------")

# Test 2
grid2 = [[0, 1, 1, 0],
         [0, 1, 1, 0]]
update(grid2, 2, 4)
print("Expected result:", [[0, 1, 1, 0], [0, 1, 1, 0]])
print("Actual result:  ", grid2)
       
print("------")

# Test 3
grid3 = [[1, 1, 1],
         [1, 0, 1],
         [1, 1, 1]]
update(grid3, 3, 3)
print("Expected result:", [[1, 0, 1], [0, 0, 0], [1, 0, 1]])
print("Actual result:  ", grid3)

print("------")

update(grid3, 3, 3)
print("Expected result:", [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print("Actual result:  ", grid3)
"""

### Game

life.start(500, update)