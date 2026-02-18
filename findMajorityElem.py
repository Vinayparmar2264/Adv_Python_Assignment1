# 25. Find Majority Element: Find the element that appears more than n/2 times.
def findMajorityElem(nums):
    my_dict = {}
    for i in range(len(nums)):
        if nums[i] not in my_dict:
            my_dict[nums[i]]=1
        else:
            my_dict[nums[i]]+=1
    n = len(nums)
    for k,v in my_dict.items():
        if v>n//2:
            return k
        
nums = [2,1,3,4,5,2,2,2,2]
print(findMajorityElem(nums))

# optimal solution with the help of the Moore's Algo.:-

def Moore_sAlgo(nums):
    freq = 0
    ans = 0
    for i in range(1,len(nums)):
        if freq==0:
            ans=nums[i]
        if nums[i]==ans:
            freq+=1
        else:
            freq-=1
    return ans

nums = [2,1,3,3,5,5,3,5,5,5,5,5]
print(Moore_sAlgo(nums))
    