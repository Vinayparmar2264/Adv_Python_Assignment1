# 21. Find the Kth Smallest Element

def merge_arr(left,right):
    i = 0
    j = 0
    result = []
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        elif left[i]>right[j]:
            result.append(right[j])
            j+=1
    while i<len(left):
        result.append(left[i])
        i+=1
    while j < len(right):
        result.append(right[j])
        j+=1

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



def KthSmallestEle(nums,k):
    my_set = set(nums)
    new_nums = list(my_set)
    sorted_arr = merge_sort(new_nums)
    return sorted_arr[k-1]

nums = [3,2,5,4,6,7,8,9,2]
print(KthSmallestEle(nums,3))