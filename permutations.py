def getPermutations(array):
	permutations = []
	getPermutationsHelper(array, [], permutations)
	return permutations

def getPermutationsHelper(array, nowPerm, permutations):
	
	if (not len(array) and len(nowPerm)):
		permutations.append(nowPerm)
		
	else:
		for i in range(len(array)):
			new = array[:i] + array[1+i:]
			newPerm = nowPerm + [array[i]]
			getPermutationsHelper(new, newPerm, permutations)
			 

print(getPermutations([1,2,3]))