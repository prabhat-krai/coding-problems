# The Next greater Element for an element x is the first 
# greater element on the right side of x in array.

def next_larger_entry(arr): 
    result = []
    for i in range(0, len(arr)): 
        next = -1
        for j in range(i+1, len(arr)): 
            if (arr[i] < arr[j]): 
                next = arr[j] 
                break
        result.append(next)      
    return result
  

def test():
    arr = [11,13,21,3] 
    assert next_larger_entry(arr) == [13,21,-1,-1]
    arr = [1,2,3,4,5]
    assert next_larger_entry(arr) == [2,3,4,5,-1]

    print('tests passed')

test()