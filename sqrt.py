def root_2(num):
    low = 0.0
    high = num + 1
    mid = (low + high) / 2 
    while(mid >= low):

        val = mid*mid 

        if(val > num):
            high = mid 
            mid = (low + high) / 2

        if (val == num): 
            return mid 
        
        if (val < num):
            low = mid 
            mid = (low + high) / 2
    return low   

print(root_2(10000005820000000))