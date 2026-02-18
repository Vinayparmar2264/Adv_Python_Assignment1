# 12. Find the Missing Number: Find the missing number in an array of size n containing numbers from 1 to n.
def findMissNum(nums):
    n = nums[-1]
    actual_sum=0
    total_sum = n*(n+1)/2
    for num in nums:
        actual_sum+=num
    return int(total_sum-actual_sum)


nums = [1,2,4,5]
print(findMissNum(nums))