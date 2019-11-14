#coding ques asked by google

#given different heights of dams find the max volume 
#of water they can hold between them. 

def find_water_volume(heights):
    max_vol = 0
    for i in range(len(heights) - 1):
        #trying all permutations
        for j in range(i+1, len(heights)):
            height_here = min(heights[i], heights[j]) 
            vol = height_here * (j - i)
            if (vol > max_vol):
                max_vol = vol 

    return max_vol

def test():
    assert find_water_volume([1,5,1,1,1,5,80]) == 25
    assert find_water_volume([1,5,1,1,1,5,4]) == 20
    assert find_water_volume([]) == 0
    print("Passed")

test()