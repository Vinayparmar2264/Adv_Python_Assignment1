# 1. Reverse an Array
def reverseArray(nums):
    i=0
    j=len(nums)-1
    while i<=j:
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
        j-=1
    return nums
nums = [1,2,3,4,5]
print(reverseArray(nums))