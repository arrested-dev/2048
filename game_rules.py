import random


def print_grid(grid):
    for row in grid:
        print(row)


def mirror_matrix(matrix):
    for i in range(len(matrix)):
        row = matrix[i]
        j0,  j1 = 0, len(row) - 1
        while j1 >= j0:
            matrix[i][j0], matrix[i][j1] = matrix[i][j1], matrix[i][j0]
            j0 += 1; j1 -= 1
    return matrix


def rotate_matrix_cw(grid):
    new_grid = []
    for j in range(len(grid[0])):
        row = []
        for i in range(len(grid)):
            row.append(grid[i][j])
        new_grid.append(row)
    mirror_matrix(new_grid)
    return new_grid
    
    
def rotate_matrix_acw(grid):
    mirror_matrix(grid) 
    new_grid = []
    for j in range(len(grid[0])):
        row = []
        for i in range(len(grid)):
            row.append(grid[i][j])
        new_grid.append(row)
    return new_grid

##def left(grid):
##    for i in range(len(grid)):
##        for j in range(1,4):
##            if grid[i][j] != 0:
##                k = j
##                while k > 0 and grid[i][k-1] == 0:
##                    k -=1
##                if grid[i][k] == 0:
##                    grid[i][k] = grid[i][j]
##                    grid[i][j] = 0
##    return grid

def perform_left_merges(grid):
    for i in range(len(grid)):
        while 1:
            c = 0
            for j in range(1, len(grid[i])):
                if grid[i][j] != 0 and grid[i][j-1] == grid[i][j]:
                    c += 1
                    grid[i][j-1] = grid[i][j-1] + grid[i][j]
                    grid[i][j] = 0
            if c == 0:
                break
    return grid

def left(grid):
    for i in range(len(grid)):
        for j in range(1, len(grid[i])):
            if grid[i][j] != 0:
                k = j
                while k > 0 and grid[i][k-1] == 0:
                    k -=1
                if grid[i][k] == 0:
                    grid[i][k] = grid[i][j]
                    grid[i][j] = 0
    return perform_left_merges(grid)



def right(grid):
    return mirror_matrix(left(mirror_matrix(grid)))

def top(grid):
    return rotate_matrix_cw(left(rotate_matrix_acw(grid)))

def bottom(grid):
    return mirror_matrix(rotate_matrix_acw(left(rotate_matrix_cw(grid))))


def points_left(grid):
    def count_occurences(_array, count):
        c = 0
        for i in _array:
            if count == i:
                c += 1
        return c

    points = 0
    for i in range(len(grid)):
        buffer = []
        for j in range(0, len(grid[i])):
            if grid[i][j] != 0:
                buffer.append(grid[i][j])
        while 1:
            c  = 0
            for k in range(1, len(buffer)):
                if buffer[k-1] == buffer[k]:
                    c += 1
                    points += (buffer[k-1] + buffer[k])
                    del buffer[k-1]
                    del buffer[k-1]
                    break
            if c ==0:
                break
    return points


def points_right(grid):
    points = points_left(mirror_matrix(grid))
    mirror_matrix(grid)
    return points

def points_top(grid):
    points = points_left(rotate_matrix_acw(grid))
    rotate_matrix_cw(grid)
    return points


def points_bottom(grid):
    points = points_left(rotate_matrix_cw(grid))
    rotate_matrix_acw(grid)
    return points




def determine_best_move(grid):
    points = []
    points.append(points_left(grid))
    points.append(points_top(grid))
    points.append(points_bottom(grid))
    points.append(points_right(grid))
    print(points)
    best_move = ['left', 'up', 'down', 'right'][points.index(max(points))]
    print('best move', best_move)
    return best_move


def generate_zero_grid():
    return [[0 for j in range(4)] for i in range(4)]


def generate_rand_grid():
    grid = [[0 for j in range(4)] for i in range(4)]
    for i in range(10):        
        grid[random.randint(0,3)][random.randint(0,3)] = [2,4,2,4][random.randint(0,3)]
    return grid



if __name__ == '__main__':
    grid = [[0 for j in range(4)] for i in range(4)]

    print_grid(grid)

    for i in range(10):        
        grid[random.randint(0,3)][random.randint(0,3)] = [2,4,2,4][random.randint(0,3)]

    print('')
    print_grid(grid)

    print('') 

    print(determine_best_move(grid))
    
    print("")
    
##    print_grid(grid)


## TODO:
#- rotate matrix for different swipes
#+ assign points to every swipe
#+ merge LRTB in case of addition


