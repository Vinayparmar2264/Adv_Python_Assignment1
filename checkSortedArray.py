# 6. Check if Array is Sorted
def isArraySorted(nums):
    for i in range(len(nums)-1):
        if nums[i]<nums[i+1]:
            continue
        else:
            return False
    return True

nums = [1,2,3,8,4,5,6]
print(isArraySorted(nums))