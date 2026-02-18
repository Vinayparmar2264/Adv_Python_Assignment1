# 13. Find Duplicates in an Array
def findDuplicateEle(nums):
    my_dict = {}
    for i in range(len(nums)):
        if nums[i] not in my_dict:
            my_dict[nums[i]]=1
        else:
            my_dict[nums[i]]+=1
    ans = []
    for k,v in my_dict.items():
        if v>1:
            ans.append(k)
    return ans

nums = [1,2,4,5,6,6]
print(findDuplicateEle(nums))