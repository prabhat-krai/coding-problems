def singleNumber(nums):
	store = {}
	for num in nums:
		if num in store:
			store[num]+=1
		else:
			store[num] = 1
	for num in nums:
		if store[num] == 1:
			return num

print(singleNumber([2,2,1]))
