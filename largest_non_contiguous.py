#solving the problem of max sum where the elements forming the sum
#are not contiguous

def sum_not_contiguous(arr):
    current_max = 0
    max_so_far = 0

    for current_element in arr:
        new_max = max_so_far if max_so_far > current_max else current_max
        current_max = max_so_far + current_element
        max_so_far = new_max

    return (max_so_far if max_so_far > current_max else current_max)

arr = [5,5,10,100,1000,50]
print(sum_not_contiguous(arr))