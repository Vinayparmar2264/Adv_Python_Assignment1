# 8. Find Pair with Given Sum: Find a pair of elements that adds up to a target sum.
def PairSum(nums,target):
    my_set = set()
    for i in range(len(nums)):
        temp = target-nums[i]
        if temp in my_set:
            return temp,nums[i]
        my_set.add(nums[i])

nums = [5,1,2,3,4,9,8,7,6]
target = 10
print(PairSum(nums,0))