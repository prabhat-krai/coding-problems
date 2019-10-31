# The Next greater Element for an element x is the first 
# greater element on the right side of x in array.

def next_larger_entry(arr): 
    result = []
    for i in range(0, len(arr), 1): 
        next = -1
        for j in range(i+1, len(arr), 1): 
            if arr[i] < arr[j]: 
                next = arr[j] 
                break
        result.append(next)      
    return result
  
arr = [11,13,21,3] 
print(next_larger_entry(arr))