# 19. Find Subarray with Given Sum.
def SubArrWithGivenSum(nums,total):
    i = 0 
    j = 0
    temp_sum = 0
    while j<len(nums) and i<len(nums):
        if temp_sum==total:
            return nums[i:j]
        if temp_sum<total:
            temp_sum += nums[j]
            j+=1
        elif temp_sum>total:
            temp_sum-=nums[i]
            i+=1
    if temp_sum==total:
        return nums[i:j]
nums = [4,5,2,1,1]
total=13
print(SubArrWithGivenSum(nums,total))