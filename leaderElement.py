# 17. Find the Leader Elements: An element is a leader if it is greater than all elements to its right.
def leaderElements(nums):
    n = len(nums)
    leader = []
    if n==0:
        return leader
    leader.append(nums[-1])
    max_num = nums[-1]
    for i in range(n-2,-1,-1):
        if nums[i]>max_num:
            leader.append(nums[i])
            max_num=nums[i]
    return leader


nums = [150,4,3,7,8,2,4,10,35,56,7]
print(leaderElements(nums))
