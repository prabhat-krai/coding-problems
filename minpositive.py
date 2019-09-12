"""
Given an array of integers, find the first missing positive integer in linear time 
and constant space. In other words, find the lowest positive integer that does not exist
in the array. The array can contain duplicates and negative numbers as well.

"""
import math

def seperate_posandneg(num, size):
    j=0
    for i in range(size):
        if (num[i] <= 0):
            temp = num[i]
            num[i]= num[j]
            num[j]=temp

            j+=1

    return num, j


def findMissing(arr, size):
    for i in range(size):
        x=int(math.fabs(arr[i]))
        if( x - 1 < size and arr[x-1] > 0):
            arr[x-1]= -1 * arr[x-1] 
    i=0
    for i in range(size):
        if (arr[i] > 0):
            return i+1

    return size+1


def form_arrray(arr, size):

    arr_sep, negs= seperate_posandneg(arr, len(arr))
    j=0
    arr2=[None]*(size-negs)
    for i in range (negs, size):
        arr2[j]=arr_sep[i]
        j+=1

    return findMissing(arr2, len(arr2))



a=[1, 3, -4, 22, -5]

print(form_arrray(a, len(a)))