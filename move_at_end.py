def moveElements(nums, move):
    start = 0 
    end_pointer = len(nums) - 1
    
    while(start < end_pointer):
        while(start < end_pointer and nums[end_pointer] == move):
            end_pointer -= 1
        if(nums[start] == move):
            nums[start], nums[end_pointer] = nums[end_pointer], nums[start]
            end_pointer -= 1
        start += 1
    
    return nums

print(moveElements([2,2,2,2,2,2,6,6,6,6,6,6,6,6,2,2,2,2,2,2,2], 2))