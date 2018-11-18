"""
This program makes a new array where every element is replaced my the total
product of all elements divided by the element at that position in original array.
division is allowed.

"""
def modarray(num, product):
    new_array=[product//num[i] for i in range(len(num))]

    return new_array

num=[1,2,3,4,5,6,7,8,9,10]
product=1
for j in range(len(num)):
    product=product*num[j]

print(modarray(num, product))



