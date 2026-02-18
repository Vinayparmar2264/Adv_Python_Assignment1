# 14. Find Intersection of Two Arrays: Find the common elements between two arrays.
def Intersection(nums1,nums2):
    ans=[]
    my_dict = {}
    n = len(nums1)
    m = len(nums2)
    for i in range(len(nums1)):
        if nums1[i] not in my_dict:
            my_dict[nums1[i]]=0
    for i in range(len(nums2)):
        if nums2[i] in my_dict:
            ans.append(nums2[i])
            my_dict.pop(nums2[i])
    return ans

nums1 = [1,2,3,4,5,6,7,8,8,6,5,4,0]
nums2 = [3,0,4,4,4,50,40]
print(Intersection(nums1,nums2))