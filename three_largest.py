def findThreeLargestNumbers(array):
    # Write your code here.
    three = array[:3]
    for i in range(3, len(array)):
        j = minimum(three)
        if(array[i]>three[j]):
            three[j] = array[i]
    three = sorted(three)
    return three

def minimum(arr):
    k=0
    mini = arr[0]
    for i in range(1,len(arr)):
        if (arr[i] < mini):
            mini = arr[i]
            k = i
			
    return k

print(findThreeLargestNumbers([7,8,3,11,43,55]))