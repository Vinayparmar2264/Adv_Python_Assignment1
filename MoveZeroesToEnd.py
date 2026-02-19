# 18. Move Zeroes to End: Move all zeroes in an array to the end while maintaining the order of non-zero elements.
def MoveZeroToEnd(nums):
    i=0
    j=0
    while j<len(nums) and i<len(nums):
        if nums[j]!=0 and i==j:
            i+=1
            j+=1
        elif nums[j]!=0 and i!=j:
            nums[i],nums[j] = nums[j], nums[i]
            i+=1
            j+=1
        elif nums[j]==0:
            j+=1
    return nums
nums = [3,4,0,0,4,6,2,0,1,0]

print(MoveZeroToEnd(nums))
