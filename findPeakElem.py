# 26. Find Peak Element: A peak element is greater than its neighbors. Find one such element.
# Broute Force approach
def peakElem(nums):
    for i in range(len(nums)-1):
        if nums[i]<nums[i+1]:
            continue
        elif nums[i]>nums[i+1] and nums[i]>nums[i-1]:
            return nums[i]
        
        
nums = [1,2,3,4,5,10,8,9]
print(peakElem(nums))