# 22. Find All Subarrays
def AllSubArr(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            result.append(nums[i:j+1])
    return result

nums = [1,2,3]
print(AllSubArr(nums))