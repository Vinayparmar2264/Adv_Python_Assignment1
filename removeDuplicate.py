# 9. Remove Duplicates from Array: Remove duplicates from the array while maintaining order.
def removeDuplicate(nums):
    my_dict={}
    ans = []
    for i in range(len(nums)):
        if nums[i] not in my_dict:
            my_dict[nums[i]]=1
    for k,v in my_dict.items():
        ans.append(k)
    return ans
nums = [2,2,3,4,4]
print(removeDuplicate(nums))
