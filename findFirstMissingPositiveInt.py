# 27. Find the First Missing Positive: Find the smallest positive integer missing in the array.

def FirstMissNum(nums):
    flag = False
    for i in range(len(nums)):
        if nums[i]<=0:
            nums[i]=1
        elif nums[i]>len(nums):
            nums[i]=1
        elif nums[i]==1:
            flag = True
    print(nums)
    if flag==False:
        return 1
    
    else:
        for i in range(len(nums)):
            temp = abs(nums[i])
            idx = temp-1
            if nums[idx]>0:
                nums[idx]=nums[idx]*(-1)
        print(nums)
        for i in range(len(nums)):
            if nums[i]<0:
                continue
            else:
                return i+1
            
nums = [2,5,3,-1,1]
print(FirstMissNum(nums))