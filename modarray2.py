"""
This program makes a new array where every element is replaced my the total
product of all elements divided by the element at that position in original array.
Division is not allowed
"""

def develop_arrays(arr):
    left_array=[None]*len(arr)
    right_array=[None]*len(arr)
    left_array[0]=1
    for i in range(1,len(arr)):
        left_array[i]=left_array[i-1]*arr[i-1]

    right_array[len(arr)-1]=1
    j=len(arr)-2
    while(j>-1):
        right_array[j]=right_array[j+1]*arr[j+1] 
        j-=1   
    return left_array, right_array

def new_array(l_array, r_array):
    new_array=[l_array[i]*r_array[i] for i in range(len(l_array)) ]
    return new_array

num=[1,2,3,4,5,6,7,8,9,10]
l_array, r_array=develop_arrays(num)
print(new_array(l_array,r_array))

