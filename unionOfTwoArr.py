# 15. Find Union of Two Arrays
def Union(nums1,nums2):
    ans=[]
    my_dict = {}
    n = len(nums1)
    m = len(nums2)
    for i in range(len(nums1)):
        if nums1[i] not in my_dict:
            my_dict[nums1[i]]=0
    for i in range(len(nums2)):
        if nums2[i] not in my_dict:
            my_dict[nums2[i]]=0
    for k,v in my_dict.items():
        ans.append(k)
    return ans

nums1 = [1,2,1,1,1,3,4,5]
nums2 = [1,1,1,2,3,4,5,6,7,8,9]
print(Union(nums1,nums2))