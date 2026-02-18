# 5. Count Frequency of Elements
def FreqofElem(nums):
    my_dict = {}
    for i in range(len(nums)):
        if nums[i] not in my_dict:
            my_dict[nums[i]]=1
        else:
            my_dict[nums[i]]+=1
    return my_dict

nums = [2,3,2,3,2,3,2,1]
print(FreqofElem(nums))