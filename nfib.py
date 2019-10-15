import timeit
memo = [None] * 1000


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
	if (n == 1):
		return 0
	if (n == 2):
		return 1	
	else:
		return getNthFibRec(n - 1) + getNthFibRec(n - 2)


def getNthFibRecDP(n, memo):
	if (n == 2 or n==3):
		memo[n] = 1
	if(memo[n] is None):
		memo[n] = getNthFibRecDP(n - 1, memo) + getNthFibRecDP(n - 2, memo)
	
	return memo[n]



def wrapper(func, *args, **kwargs): # wrapper for function to time them
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

exp = 1  # number of times to run them
fib = 40 # which fib number

wrapped = wrapper(getNthFibIter, fib)
print("Iteration Time : ",timeit.timeit(wrapped, number = exp))
wrapped = wrapper(getNthFibRecDP, fib, memo)
print("Recursion Time with DP : ",timeit.timeit(wrapped, number = exp))
wrapped = wrapper(getNthFibRec, fib)
print("Recursion Time : ",timeit.timeit(wrapped, number = exp))
