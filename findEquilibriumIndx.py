# 31. Find Equilibrium Index: Find an index such that sum of elements on left = sum on right.
def EquilibriumInx(nums):
    total_sum = 0
    for i in range(len(nums)):
        total_sum+=nums[i]
    left_sum = total_sum//2
    temp_sum =0
    for i in range(len(nums)):
            temp = total_sum - nums[i]
            if temp_sum == temp/2:
                return i
            elif temp_sum!=temp/2 and temp_sum<=left_sum:
                temp_sum+=nums[i]
    return "Equilibrium index is not exist in this given array"
    

nums = [25,5,5,15,10,5]
print(EquilibriumInx(nums))

