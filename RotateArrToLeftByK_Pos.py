# 20. Rotate Array to the Left by k Positions
def ArrRotateByK(nums,pos):
    i = 0 
    j = pos-1
    while i<j:
        nums[i],nums[j] = nums[j],nums[i]
        i+=1
        j-=1

    i = pos
    j = len(nums)-1
    while i<j:
        nums[i],nums[j] = nums[j],nums[i]
        i+=1
        j-=1

    i = 0 
    j = len(nums)-1
    while i < j :
        nums[i],nums[j] = nums[j],nums[i]
        i+=1
        j-=1
    return nums

nums = [1,2,3,4,5,6,7,8,9]
pos = 3
print(ArrRotateByK(nums,pos))   