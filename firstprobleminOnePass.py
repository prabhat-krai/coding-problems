"""
This program finds if a pair of numbers that equal to a user inputted number. 
This does this using one pass by using hashing

"""

def findPairs(A, A_size, sum):

    numbers=set()

    for x in range (0, A_size):
        comp=sum-A[x]
        if (comp>0 and comp in numbers):
            print ("Pair with the given sum,",sum,",is", A[x] , comp)
        numbers.add(A[x])

a=[1,2,7,2,6,2,6,8,5,3,2,6,8,9,10,16,23,14,22,25,28]
k=24
findPairs(a,len(a),k)


