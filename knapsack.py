def knapsack(items, weight_bag):
    values = [[0 for i in range(weight_bag + 1)]for j in range(len(items) + 1)]
    for i in range(1, len(items)+1):
        weight_comp = items[i-1][1]
        value = items[i-1][0]
        for x in range(weight_bag + 1):
            if (weight_comp > x):
                values[i][x] =  values[i-1][x]
            else:
                values[i][x] = max(values[i-1][x], values[i-1][x - weight_comp] + value) 
    
    return values[-1][-1]

print(knapsack([[1,4],[2,5],[5,6],[7,2]], 15))
    

