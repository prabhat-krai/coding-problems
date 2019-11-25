def findClosestValueInBst(tree, target):
	return findClosestValueInBstHelper(tree, target, float("inf"))
	
def findClosestValueInBstHelper(tree, target, closest):
	if (tree is None):  #base case
		return closest
	if (abs(target - closest) > abs(target - tree.value)): #assigning new closest value
		closest = tree.value
	
	if (target > tree.value):
		return findClosestValueInBstHelper(tree.right, target, closest)
	elif(target < tree.value):
		return findClosestValueInBstHelper(tree.left, target, closest)
	else:
		return closest