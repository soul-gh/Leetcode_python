#最大连续子集合

#超时
class Solution:
    def maxSubArray(nums) -> int:
        n = len(nums)
        max1 = -float('inf')
        for i in range(n):
            cur = 0
            for j in range(i,n):
                cur += nums[j]
                if cur > max1:
                    max1 = cur
        return max1
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution.maxSubArray(nums))

#DP   d:以第i个数为结尾的最大子集合
class Solution1:
    def maxSubArray(nums) -> int:
        n= len(nums)
        d = [0]*(n+1)
        for i in range(1,n+1):
            d[i] = max(nums[i-1],d[i-1] + nums[i-1])
        return max(d[1:])
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution.maxSubArray(nums))