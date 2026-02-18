# 33. Find Maximum Difference (j > i)
def findMaxDiff(nums):
    max_num = float("-inf")
    min_num = float("inf")
    for i in range(len(nums)):
        if nums[i]>max_num:
            max_num=nums[i]
        if nums[i]<min_num:
            min_num=nums[i]
    return max_num-min_num

nums = [3,4,6,4,2,7,3,6,9]
print(findMaxDiff(nums))