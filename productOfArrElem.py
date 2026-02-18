# 30. Product of Array Except Self
# Given an array, return a new array where each element is the product of all elements except itself.
# Do not use division.

# Input: [1,2,3,4]
# Output: [24,12,8,6]

def ProductArrElem(nums):
    prod = 1
    count = 0
    flag = False
    for i in range(len(nums)):
        if nums[i]!=0:
            prod*=nums[i]
        else:
            flag = True
            count+=1
    result = []
    if flag==False:
        for i in range(len(nums)):
            result.append(prod//nums[i])
        return result
    elif flag==True and count<2:
        for i in range(len(nums)):
            if nums[i]==0:
                result.append(prod)
            else:
                result.append(0)
        return result
    elif flag == True and count>=2:
        result = [0]*len(nums)
        return result

nums = [1,2,8,3,4,0]
print(ProductArrElem(nums))