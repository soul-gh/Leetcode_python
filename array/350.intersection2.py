class Solution:
    def intersect(nums1, nums2):
        nums1.sort()
        nums2.sort()
        res = []
        j = i = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                j += 1
                i += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res
nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution.intersect(nums1,nums2))