def trapped_water(height):
    # if there are less than 3 ele, water can't trapped
    if not height or len(height) < 3:
        return 0
        
    # Initialize pointers
    left = 0
    right = len(height) - 1
    
    # store height
    left_max = height[left]
    right_max = height[right]
    
    # store total water trapped
    trapped_water = 0
    
    # Iterate until left and right pointers meet
    while left<right:
        # if left is lower then process with left side
        if left_max < right_max:
            # move left pointer
            left += 1
            if height[left] > left_max:
                # update left max
                left_max = height[left]
            else:
                # add trapped water on left side
                trapped_water += left_max - height[left]
        else:
            # move pointer to right pointer
            right -= 1
            if height[right] > right_max:
                # update right max
                right_max = height[right]
            else:
                trapped_water += right_max - height[right]
    return trapped_water
    
# function call
arr = [2, 1, 3, 0, 1, 2, 3]
result = trapped_water(arr)
print(f"{result} units of water will be trapped")

# output
# 7 units of water will be trapped
    