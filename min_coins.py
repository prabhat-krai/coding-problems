def find_min_coins(n, denominations):
    coins = [float("inf") for a in range (n+1)]
    coins[0] = 0
    for denomination in denominations:
        for amount in range(n + 1):
            if(denomination <= amount):
                coins[amount] = min(coins[amount] , coins[amount - denomination] + 1)

    result = -1 if coins[n] == float("inf") else coins[n]
    return result

print(find_min_coins(9,[1,5,10]))