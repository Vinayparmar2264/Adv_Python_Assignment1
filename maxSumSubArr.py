# 23. Maximum Sum Subarray (Kadane's Algorithm)
def MaxSumSubArr(nums):
    maxi = float("-inf")
    total =0
    for i in range(len(nums)):
        total+=nums[i]
        maxi=max(maxi,total)
        if nums[i]<0:
            total=0
    return maxi
        
nums = [2,-1,-1,-2,-3]
print(MaxSumSubArr(nums))