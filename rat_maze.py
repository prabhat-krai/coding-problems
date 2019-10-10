# a rat is in a maze that has co-ordinates that are blocked off
# We need to find a path(not the shortest) that helps the rat to 
# move from (0,0) to (N,N)

N = 4 #size of the maze 

def printPath(sol):
    sol[N-1][N-1] = 1
    for i in range(N):
        for j in range(N):
            print(sol[i][j], end=" ")
        print("\n")

def solveMaze(maze):
    if (maze[0][0] == 0):
        return False
    solution = [[0 for _ in range(N)] for _ in range(N)]

    if(solveMazeHelper(maze, 0, 0, solution) == False):
        return False

    else:
        #printPath(solution)  # remove comment for path
        return True


def isSafe(maze, x, y):

    if(x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1):
        return True
    else:
        return False


def solveMazeHelper(maze, x, y, sol):
    
    if(x == N-1 and y == N-1 and maze[x][y] == 1):
        return True

    if isSafe(maze, x, y):
        sol[x][y] = 1

        if (solveMazeHelper(maze, x+1, y, sol) == True):
            return True

        if (solveMazeHelper(maze, x, y+1, sol) == True):
            return True

        sol[x][y] = 0
        return False


def test():
    maze = [ [1, 0, 1, 0], 
        [1, 1, 1, 1], 
        [0, 1, 0, 1], 
        [1, 1, 1, 1]] 
    assert solveMaze(maze) == True

    maze = [ [1, 0, 1, 0], 
        [1, 1, 1, 1], 
        [0, 1, 0, 1], 
        [1, 1, 1, 0]] 
    assert solveMaze(maze) == False

    maze = [ [1, 0, 1, 0], 
        [1, 1, 1, 1], 
        [0, 1, 0, 0], 
        [1, 1, 0, 1]] 
    assert solveMaze(maze) == False

    maze = [ [0, 0, 1, 0], 
        [1, 1, 1, 1], 
        [0, 1, 0, 1], 
        [1, 1, 1, 1]] 
    assert solveMaze(maze) == False

    maze = [ [1, 0, 1, 0], 
        [1, 1, 0, 1], 
        [0, 0, 0, 1], 
        [1, 1, 1, 1]] 
    assert solveMaze(maze) == False
    print('Tests passed')

test()