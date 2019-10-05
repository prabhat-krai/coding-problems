"""
Given a left and right ends of a list. 
Find all the numbers between the two that sum to N.
"""

left = int(input("Left end"))
right = int(input("Right end"))
sum_total = int(input("Sum"))

#naive solution

def get_sum(num, sum_total):
    num_sum = 0
    while(num > 0 and num_sum <= sum_total):
        d = num % 10
        num_sum += d
        num = num // 10
    return num_sum

count = 0
for i in range(left, right+1):
    num_sum = get_sum(i, sum_total)
    if(num_sum == sum_total):
        count += 1

print(count)


#Dynammic Programming


