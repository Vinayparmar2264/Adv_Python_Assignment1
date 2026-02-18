# 16. Check if Two Arrays Are Equal: if two arrays contain the same elements
def isTwoArrEqual(nums1,nums2):
    n = len(nums1)
    m = len(nums2)
    if m!=n:
        return False
    my_dict = {}
    for i in range(len(nums1)):
        if nums1[i] not in my_dict:
            my_dict[nums1[i]]=1
        else:
            my_dict[nums1[i]]+=1
    my_dict2={}
    for i in range(len(nums2)):
        if nums2[i] not in my_dict2:
            my_dict2[nums2[i]]=1
        else:
            my_dict2[nums2[i]]+=1
    for k,v in my_dict.items():
        if k in my_dict2:
            if my_dict2[k]==v:
                continue
            else:
                return False
    return True

nums1 = [ 1,3,4,5,6,4,2,3,1,5]
nums2 = [ 1,3,4,5,6,4,2,3,1]

print(isTwoArrEqual(nums1,nums2))

