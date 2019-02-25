def binarySearch(array, target):
	lower = 0
	upper = len(array) - 1
	mid = (lower+upper)//2
	while(lower <= upper):
        if(target == array[mid]):
        	return mid
		elif(target < array[mid]):
			upper = mid - 1
			mid = (lower+upper)//2
		else:
			lower = mid + 1
			mid = (lower+upper)//2
	return -1

print(binarySearch([1,2,3,4,5], 4))