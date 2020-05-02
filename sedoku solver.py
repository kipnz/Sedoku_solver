#a backtracking algorithm to solve sudoku puzzles

def main():
        grid=[[3,0,6,5,0,8,4,0,0], 
        [5,2,0,0,0,0,0,0,0], 
        [0,8,7,0,0,0,0,3,1], 
        [0,0,3,0,1,0,0,8,0], 
        [9,0,0,8,6,3,0,0,5], 
        [0,5,0,0,9,0,6,0,0], 
        [1,3,0,0,0,0,2,5,0], 
        [0,0,0,0,0,0,0,7,4], 
        [0,0,5,2,0,6,3,0,0]]

        if(solve(grid)):
            for i in range(9):
                for j in range(9):
                    print(grid[i][j], end = " ")
                print()
        else:
            print('No Solution available')

def check_square(grid, row, column, num):
    row = (row // 3) * 3
    column = (column // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[row+i][column+j] == num:
                return True
    return False

def check_row(grid, row, num):
    for i in range(9):
        if grid[row][i] == num:
            return True
    return False


def check_column(grid, column, num):
    for i in range(9):
        if grid[i][column] == num:
            return True
    return False

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return [i, j]
    return False

def solve(grid):
    location = find_empty(grid)
    if location == False:
        return True
    else:
        row = location[0]
        column = location[1]
        

    for i in range(1, 10):
        if not check_column(grid, column, i) and not check_row(grid, row, i) and not check_square(grid, row, column, i):
            grid[row][column] = i
            if(solve(grid)):
                return True
            grid[row][column] = 0
    return False

main()
