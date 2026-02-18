# 11. Remove given Element from Array
# 12. Find the Missing Number: Find the missing number in an array of size n containing numbers from 1 to n.
# 13. Find Duplicates in an Array
# 14. Find Intersection of Two Arrays: Find the common elements between two arrays.
# 15. Find Union of Two Arrays
# 16. Check if Two Arrays Are Equal: if two arrays contain the same elements
# 17. Find the Leader Elements: An element is a leader if it is greater than all elements to its right.
# 18. Move Zeroes to End: Move all zeroes in an array to the end while maintaining the order of non-zero elements.
# 19. Find Subarray with Given Sum.
# 20. Rotate Array to the Left by k Positions

def removeGivenEle(nums,k):
    i = 0
    while i<len(nums):
        if nums[i]==k:
            nums.remove(k)
        i+=1
    return nums
nums = [3,4,4,3,1,5,6,7,8,3]
print(removeGivenEle(nums,3))
