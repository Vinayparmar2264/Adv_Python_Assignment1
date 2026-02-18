# 32. Find Maximum Product Pair: Find two elements whose product is maximum.
def MaxProdPair(nums):
    max_num = float("-inf")
    second_largest = float("-inf")
    for i in range(len(nums)):
        if nums[i]>max_num:
            temp = max_num
            max_num=nums[i]
        elif second_largest<temp:
            second_largest = temp
        elif nums[i]>second_largest and nums[i]>temp and nums[i]<=max_num:
            second_largest=nums[i]
        
    return max_num,second_largest
nums = [1,2,4,5,6,7,3,7,9,9,10]    
print(MaxProdPair(nums))