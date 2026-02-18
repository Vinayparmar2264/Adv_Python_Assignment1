# 4. Find the Second Largest Element
def secondLargestEle(nums):
    max_num = float("-inf")
    second_largest = float("-inf")
    for i in range(len(nums)):
        if nums[i]>max_num:
            temp = max_num
            max_num=nums[i]
        if second_largest<temp:
            second_largest = temp
        if nums[i]>second_largest and nums[i]>temp and nums[i]<max_num:
            second_largest=nums[i]
        
    return second_largest
nums = [4,3,2,5,2,8,21,30,23,31,41]
print(secondLargestEle(nums))
