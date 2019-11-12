#coding ques asked by google

#given different heights of dams find the max volume 
#of water they can hold between them. 

def find_water_volume(heights):
    max_vol = 0
    for i in range(len(heights) - 1):
        #trying all permutations
        for j in range(i+1, len(heights)):
            vol = min(heights[i], heights[j]) * (j - i)
            if (vol > max_vol):
                max_vol = vol 

    return max_vol