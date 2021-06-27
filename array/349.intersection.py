#交集，暴力
class Solution:
    def intersection(nums1, nums2):
        res = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if nums1[i] not in res:
                        res.append(nums1[i])
        return res
nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution.intersection(nums1,nums2))

#微暴力， in判断
class Solution1:
    def intersection(nums1, nums2):
        res = []
        for i in nums1:
            if i in nums2 and i not in res:
                res.append(i)
        return res
nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution1.intersection(nums1,nums2))

#set去重，返回求交
class Solution2:
    def intersection(nums1, nums2):
        return list(set(nums1) & set(nums2))
nums1 = [1,2,2,1]
nums2 = [2,2]
res = Solution2.intersection(nums1,nums2)
print(res)
