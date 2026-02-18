# 10. Merge Two Sorted Arrays
def MergeTwoSortedArr(num1,num2):
    sortedArr = []
    i=0
    j=0
    while i<len(num1) and j<len(num1):
        if num1[i]<=num2[j]:
            sortedArr.append(num1[i])
            i+=1
        else:
            sortedArr.append(num2[j])
            j+=1
    while i<len(num1):
        sortedArr.append(num1[i])
        i+=1
    while j<len(num2):
        sortedArr.append(num2[j])
        j+=1
    return sortedArr

num1 = [1,2,3,4,5]
num2 = [2,3,7,8,9]
print(MergeTwoSortedArr(num1,num2))

