def isPowerOfTwo(n):
    if (n <= 0):
        return False

    n = format(n, 'b') 
    if(sum(map(int, str(n))) == 1):
        return True
    else:
        return False

print(isPowerOfTwo(2**33 + 1))