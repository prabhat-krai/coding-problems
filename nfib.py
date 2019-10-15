def getNthFibIter(n):
    # Write your code here.
	a = [0 , 1]
	if (n==1):
		return a[0]
	if (n==2):
		return a[1]
	for i in range(2, n):
		a.append(a[i-1] + a[i-2])
		
	return a[n-1]

def getNthFibRec(n):
	if (n == 1 or n==2):
		return 1
	else:
		return getNthFibRec(n - 1) + getNthFibRec(n - 2)


print(getNthFibIter(64))
print(getNthFibRec(64))