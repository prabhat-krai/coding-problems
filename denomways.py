def numberOfWaysToMakeChange(n, denoms):
    num_ways =[0 for amount in range(n+1)]
    num_ways[0] = 1
    for denom in denoms:
        for amt in range(1, n+1):
            if (amt >= denom):
                num_ways[amt] += num_ways[amt-denom]

    return num_ways[n]

print(numberOfWaysToMakeChange(9,[3,1,5]))