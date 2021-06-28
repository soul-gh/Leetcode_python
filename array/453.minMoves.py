#最少操作次数。每次操作对n-1个元素+1，最终全部相等

#转换思维，每次给一个数-1，最终全部相等
class Solution:
    def minMoves(nums):
        Min = min(nums)
        res = 0 
        for i in range(len(nums)):
            res += nums[i] - Min
        return res
nums = [1,2,3]
print(Solution.minMoves(nums))