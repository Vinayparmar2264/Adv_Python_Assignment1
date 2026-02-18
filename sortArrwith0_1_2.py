# 28. Sort an Array of 0s, 1s, and 2s: Sort an array consisting of only 0s, 1s, and 2s.
def sortArrr(nums):
    zeroes = 0
    ones=0
    twos=0
    result = []
    n = len(nums)
    for num in nums:
        if num == 0:
            result.append(0)
        elif num == 1:
            ones+=1
    temp_ones = [1]*ones
    result.extend(temp_ones)
    temp = len(nums)-len(result)
    for i in range(temp):
        result.append(2)
    return result

nums = [0,2,1,0,2,1,0,2,1,0]

print(sortArrr(nums))