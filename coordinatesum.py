def edgeSum(i):
    edgeSum = 0
    for k in range(-i+1, i):
        edgeSum += abs(i) + abs(k)
    return 4*edgeSum


def totalSum(sum):
    curr_sum = 0 
    if(sum == 0):
        return 4
    size = 1
    while(curr_sum <= sum):
        curr_sum += 4*2*size + edgeSum(size)
        if(curr_sum >= sum):
            return 8*size
        size += 1

print(totalSum(9))