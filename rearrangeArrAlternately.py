# 24. Rearrange Array Alternately: Rearrange an array such that elements alternate between the largest and smallest.
def merge_arr(left,right):
    l=0
    r=0
    result = []
    while l<len(left) and r<len(right):
        if left[l]<=right[r]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
    while l<len(left):
        result.append(left[l])
        l+=1
    while r<len(right):
        result.append(right[r])
        r+=1
    return result

def merge_sort(nums):
    if len(nums)<=1:
        return nums
    mid = len(nums)//2
    left_half = nums[:mid]
    right_half = nums[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge_arr(left_half,right_half)


def rearrangeArr(nums):
    nums = merge_sort(nums)
    ans = []
    i=0
    j=len(nums)-1
    while i<=j:
        if i==j:
            ans.append(nums[i])
        else:

            ans.append(nums[j])
            ans.append(nums[i])
        j-=1
        i+=1
    return ans
nums = [5,4,7,9,1,2,6,3,8]
print(rearrangeArr(nums))