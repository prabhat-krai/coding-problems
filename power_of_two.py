def isPowerOfTwo(n):
    if (n <= 0):
        return False

    n = format(n, 'b')  # converting it into bits interpretation
    if(sum(map(int, str(n))) == 1): #if there is only one 1 in that then it is power of 2
        return True
    else:
        return False

print(isPowerOfTwo(2**33 + 1))