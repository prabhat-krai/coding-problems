"""Given a matrix of integers and coordinates of a rectangular region within the matrix, 
find the sum of numbers falling inside the rectangle."""

#The function will be called mulitple times with different rectangular regions.

matrix = [[70,23,25,12,54,54],
            [45,34,21,67,44,99],
            [12,0,89,100,21,23],
            [70,23,25,12,54,54],
            [45,34,21,67,44,99],
            [12,0,89,100,21,23]]

def matrix_region_sum_slower(matrix, A, D):
    """ A: Top left co-ordinate
        D: Bottom right co-ordinate """

    if len(matrix)==0:
        return
    totalSum=0
    for i in range(A[0], D[0]+1):
        for j in range(A[1], D[1]+1):
            totalSum+=matrix[i][j]
    return totalSum

#This solution will calculate the regions sum everytime.
#This will slow down the process.

def precompute_sums(matrix):
    """Using Dynamic programming to build the array of sums.
       This reduces the time needed to build the sums matrix."""
    topRow, bottomRow=(0, len(matrix)-1)
    leftCol, rightCol=(0, len(matrix[0])-1)
    sums=[[0]*(rightCol-leftCol+1) for i in range(bottomRow-topRow+1)]
    sums[topRow][leftCol]=matrix[topRow][leftCol]
 
    for col in range(leftCol+1, rightCol+1):
        sums[topRow][col]=sums[topRow][col-1]+matrix[topRow][col]
    for row in range(topRow+1, bottomRow+1):
        sums[row][leftCol]=sums[row-1][leftCol]+matrix[row][leftCol]
 
    for col in range(leftCol+1, rightCol+1):
        columnSum=matrix[topRow][col]
        for row in range(topRow+1, bottomRow+1):
            sums[row][col]=sums[row][col-1]+matrix[row][col]+columnSum
            columnSum+=matrix[row][col]
 
    return sums

def matrix_region_sum_fast(matrix, A, D, sums):
    """This uses the sum matrix to find the region in O(1) time.
       A and D have the same meaning as the slower version."""

    if len(matrix)==0:
        return 
 
    if A[0]==0 or A[1]==0:
        sum_to_the_top_left=0
    else:
        sum_to_the_top_left=sums[A[0]-1][A[1]-1]
 
    if A[1]==0:
        sum_to_the_left=0
    else:
        sum_to_the_left=sums[D[0]][A[1]-1]
 
    if A[0]==0:
        sum_to_the_top=0
    else:
        sum_to_the_top=sums[A[0]-1][D[1]]
 
    sum_from_origin_to_bottom_left=sums[D[0]][D[1]]
 
    return sum_from_origin_to_bottom_left - sum_to_the_top - sum_to_the_left + sum_to_the_top_left

x_limit = len(matrix[0])
y_limit = len(matrix)
print(x_limit, y_limit)
sums = precompute_sums(matrix)
inp = 'y'
while(inp == 'y'):
    print("First input is A and second prompt is for D.")
    A = list(map(int, list(input())))
    D = list(map(int, list(input())))
    if(A[0] >= x_limit or D[0] >= x_limit or A[1] >= y_limit or D[1] >= y_limit):
        print("Wrong input. Out of index. Print inside the following coordinates.")
        print(len(matrix), len(matrix[0]))
    else:
        if(A[0] <= D[0] and A[1] <= D[1]):
            print(matrix_region_sum_fast(matrix, A, D, sums))
        else:
            print("Wrong input")
    inp = input("press y to keep computing different coordinates.")