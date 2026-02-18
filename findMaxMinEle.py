# 2. Find the Maximum & Minimum Element
def findMaxMinEle(nums):
    max_num = float("-inf")
    min_num = float("inf")
    for i in range(len(nums)):
        if nums[i]>max_num:
            max_num=nums[i]
        if nums[i]<min_num:
            min_num=nums[i]
    return max_num,min_num
nums = [3,2,89,4,2,6,3,63,64,64,70]
print(findMaxMinEle(nums))