div = 0
mul = 0
n = 161 
for i in range(160, 0, -1):
    for j in range(i+1, n+1):
        mul += 1
    div += 1


total = div + mul
print(div, mul, total)