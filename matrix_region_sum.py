"""Given a matrix of integers and coordinates of a rectangular region within the matrix, 
find the sum of numbers falling inside the rectangle."""

#The function will be called mulitple times with different rectangular regions.

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

