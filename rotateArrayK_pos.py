# 7. Rotate Array by k Positions: Rotate the array to the right by k positions.
def rotateArrByK(nums,k):
    n = len(nums)
    new_arr = nums[len(nums)-k:]
    ans = new_arr + nums[:len(nums)-k]
    return ans

nums = [1,2,3,4,5,6,7]
print(rotateArrByK(nums,3))