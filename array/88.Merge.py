#合并排序
class Solution:
    def merge(nums1,m,nums2,n):
        i = j = 0
        cur = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                cur.append(nums1[i])
                i += 1
            else:
                cur.append(nums2[j])
                j += 1
        if i != m:
            for q in range(i,m):
                cur.append(nums1[q])
        elif j != n:
            for q in range(j,n):
                cur.append(nums2[q])
        for k in range(m+n):
            nums1[k] = cur[k]
nums1 = [4,5,6,0,0,0]
nums2 = [1,2,3]
m = 3
n = 3
Solution.merge(nums1,m,nums2,n)
print(nums1)

#先无序拼接后，再冒泡
class Solution1:
    def merge(nums1,m,nums2,n):
        N = m
        tmp = 0
        for num in nums2:
            nums1[N] = num
            N += 1
        for i in range(m+n-1,0,-1):
            for j in range(1,i+1):
                if nums1[j] < nums1[j-1]:
                    tmp = nums1[j-1]
                    nums1[j-1] = nums1[j]
                    nums1[j] = tmp
nums1 = [4,5,6,0,0,0]
nums2 = [1,2,3]
m = 3
n = 3
Solution1.merge(nums1,m,nums2,n)
print(nums1)
