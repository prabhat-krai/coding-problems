def getNthFib(n):
    # Write your code here.
	a = [0 , 1]
	if (n==1):
		return a[0]
	if (n==2):
		return a[1]
	for i in range(2, n):
		a.append(a[i-1] + a[i-2])
		
	return a[n-1]

print(getNthFib(64))