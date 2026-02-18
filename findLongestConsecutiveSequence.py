# 29. Find the Longest Consecutive Sequence: Find the length of the longest consecutive sequence of integers.
def LongestConsecutive (nums):
    my_set = set()
    for i in range(len(nums)):
        my_set.add(nums[i])
    longest = 0 
    
    for num in my_set:
        if num-1 not in my_set:
            x=num
            count=1
            while x+1 in my_set:
                count+=1
                x+=1
            longest = max(longest,count)        
    return longest

nums = [7,4,3,6,4,5,2,1,9,0]
print(LongestConsecutive(nums))