#A数组在B数组中的下一个最大元素
class Solution:
    def nextGreaterElement(nums1, nums2):
        res = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):  
                if nums1[i] == nums2[j]:
                    for k in range(j+1,len(nums2)):
                        if nums2[k] > nums1[i]:
                            res.append(nums2[k])
                            break
                if j == len(nums2)-1 and len(res) < i+1:
                    res.append(-1)
        return res
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(Solution.nextGreaterElement(nums1,nums2))