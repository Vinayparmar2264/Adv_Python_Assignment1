# 3. Find the Sum of Elements
def sumOfElem(nums):
    sum = 0
    for num in nums:
        sum+=num
    return sum
nums = [3,4,54,3,23,5,4,9,0]
print(sumOfElem(nums))